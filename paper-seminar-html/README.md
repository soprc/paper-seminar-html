# Paper Seminar HTML

面向中文科研组会的 Codex skill。输入一篇论文 PDF 或论文链接，可附作者项目页与指定的视频，输出可离线翻页的 HTML 文献汇报、逐页讲稿和全页预览。默认约 25 页，支持指定时长、篇幅和讲解重点。

封面右侧完整呈现论文首页。正文采用蓝色学术版式，优先保留论文原图、表格和作者演示。公式使用 LaTeX 矢量排版，方法页讲变量与监督信号，结果页交代对照、样本数和结论边界。

## 来源与致谢

本项目的论文汇报流程参考了 [zsyggg/paper-craft-skills](https://github.com/zsyggg/paper-craft-skills) 中的 [paper-deck](https://github.com/zsyggg/paper-craft-skills/tree/main/skills/paper-deck)，尤其是先梳理论文叙事、再按页组织证据并优先使用作者原图的做法。感谢原作者 zsyggg。

在此基础上，本项目针对中文科研组会制作了可离线放映的 HTML 模板，并提供 LaTeX 矢量公式、逐页讲稿、原图放大和本地视频嵌入。上游项目在其 [README](https://github.com/zsyggg/paper-craft-skills#license) 中标注采用 MIT 许可证。

## 使用

安装后，把 PDF 附到 Codex 对话中，或给出可访问的论文链接。例如：

> 用 $paper-seminar-html 把附件论文做成中文组会汇报，约 25 页。听众了解机器学习，但没读过这篇论文。详细讲清方法、训练目标和关键消融，把作者项目页的机制动画嵌到对应页。

演示时，方向键翻页，F 全屏，N 查看讲稿，G 打开目录。点击原图可放大。

## 安装

将本仓库地址发给 Codex，请它安装仓库中 `skills/paper-seminar-html` 这个 skill。也可以解压或克隆本仓库后，把整个同名 skill 目录放到个人 Codex 技能目录中。默认位置为 `~/.codex/skills/paper-seminar-html/`；如设置了 `CODEX_HOME`，使用其下的 `skills/`。下一轮对话中调用。

## 工具与依赖

- [技能说明](skills/paper-seminar-html/SKILL.md) 定义内容、证据、视觉风格与交付标准。
- [制作指南](skills/paper-seminar-html/references/authoring.md) 提供页面片段、媒体标记和命令示例。
- [离线 HTML 模板](skills/paper-seminar-html/assets/deck.html) 与打包工具可直接复用。打包需要 Python 3.9+，放映只需现代浏览器。可选公式工具使用 TeX Live 或 MiKTeX 中的 latex、dvisvgm 和指南所列宏包。

仓库提供通用制作工具。每篇论文的 PDF、图表、视频按各自来源取用，汇报中保留出处。
