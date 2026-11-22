"""Render reviewed LaTeX expressions to self-contained Computer Modern SVG paths."""
import argparse
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("expressions", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    formulas = json.loads(args.expressions.read_text(encoding="utf-8"))
    if not isinstance(formulas, dict) or not formulas or not all(
        re.fullmatch(r"[A-Za-z0-9_-]+", name) and isinstance(tex, str) and tex.strip()
        for name, tex in formulas.items()
    ):
        parser.error("Expected a nonempty mapping of safe file stems to TeX expressions.")
    for command in ("latex", "dvisvgm"):
        if not shutil.which(command):
            parser.error(f"Missing executable: {command}")
    pages = "\n".join(r"\begin{preview}$\displaystyle " + tex + r"$\end{preview}"
                      for tex in formulas.values())
    document = (r"\documentclass{article}\usepackage{amsmath,amssymb}"
                r"\usepackage[active,tightpage]{preview}\begin{document}" + "\n" +
                pages + "\n" + r"\end{document}")
    with tempfile.TemporaryDirectory() as tmp:
        job = Path(tmp)
        (job / "math.tex").write_text(document, encoding="utf-8")
        subprocess.run(["latex", "-no-shell-escape", "-interaction=nonstopmode",
                        "-halt-on-error", "math.tex"], cwd=job, check=True)
        subprocess.run(["dvisvgm", "--page=1-", "--no-fonts", "--bbox=min",
                        "--output=eq%p.svg", "math.dvi"], cwd=job, check=True)
        files = sorted(job.glob("eq*.svg"), key=lambda p: int(p.stem[2:]))
        if len(files) != len(formulas):
            raise RuntimeError("Rendered page count differs from formula count.")
        args.output.mkdir(parents=True, exist_ok=True)
        for name, file in zip(formulas, files):
            shutil.copyfile(file, args.output / (name + ".svg"))


if __name__ == "__main__":
    main()
