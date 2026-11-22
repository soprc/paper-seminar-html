# Paper Seminar HTML

面向中文科研组会的 Codex skill。可从论文 PDF 与作者项目页制作汇报，也可修订或合订已有 HTML 讲义。交付可离线翻页的 HTML 和全页预览。按汇报时长与内容决定篇幅，支持对单篇论文或单个章节指定页数。

- 每篇独立封面，右侧完整呈现 PDF 首页，左侧列出题名、作者、机构及已核实的发表与获奖信息。
- 用一个具体任务贯穿方法、训练信号与推理。优先使用原图、原表和官方视频；用 LaTeX 排公式，用指标与对照支持结论。
- 统一蓝灰配色、正文字体和轻阴影分区。流程页可逐步聚焦，仅当前步骤有蓝框；静态比较与结果页一屏完整呈现。视频随页面进入静音自动播放，离页暂停。
- 合订保留原讲义顺序、前置论文、例子、图表和演示步骤，核对跨章跳转。仅改视觉时逐页核对正文，保留来源与必要署名。

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
