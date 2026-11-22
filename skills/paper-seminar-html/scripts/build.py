"""Pack an authored HTML fragment and its marked local assets for offline slides."""
import argparse
import base64
import html
import mimetypes
import re
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slides", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--title", required=True)
    args = parser.parse_args()
    source = args.slides.resolve()
    output = args.output.resolve()
    template_path = Path(__file__).resolve().parents[1] / "assets" / "deck.html"
    if output in (source, template_path):
        parser.error("Choose an output distinct from the input and the template.")
    fragment = source.read_text(encoding="utf-8")
    if not re.search(r"<section\b", fragment, re.I):
        parser.error("No slide sections in the input.")

    def embed(match):
        path = (source.parent / match[1].strip()).resolve()
        if not path.is_relative_to(source.parent) or not path.is_file():
            parser.error(f"Missing asset or path outside the slides directory: {match[1]}")
        if path == output:
            parser.error("The output cannot be used as an asset.")
        mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        data = base64.b64encode(path.read_bytes()).decode("ascii")
        return f"data:{mime};base64,{data}"

    fragment = re.sub(r"\{\{asset:([^{}]+)\}\}", embed, fragment)
    template = template_path.read_text(encoding="utf-8")
    result = template.replace("{{TITLE}}", html.escape(args.title)).replace("<!--SLIDES-->", fragment)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(result, encoding="utf-8")


if __name__ == "__main__":
    main()
