# 从材料到成品

以本 skill 的目录为起点，assets/deck.html 是 1280×720 的等比缩放舞台。模板含样式与导航逻辑。每张幻灯片是舞台的直接子 section，正文有且只有一个主标题 h2。data-topic 供目录使用，aside 存放讲稿，small 是出处。可在任意工作目录编写内容，生成文件无需服务器。

```html
<section class="cover" data-topic="论文题名">
  <img class="paper-front" src="{{asset:media/first-page.png}}" alt="论文首页">
  <div class="veil"></div><div class="covertext">
    <div class="eyebrow">组会文献汇报</div><h2>中文学术题名</h2>
    <p class="eng">原文题名</p><p class="credit">作者与出处</p>
  </div><aside>用一个可检验的问题介绍本文。</aside>
</section>
<section data-topic="主要实验">
  <div class="eyebrow">实验结果</div><h2>比较对象与任务指标</h2>
  <div class="body25"><figure>
    <img class="zoomable" src="{{asset:media/result.png}}" alt="实验原图及坐标说明" style="height:300px">
    <figcaption>对照组、评估口径、主要差异</figcaption>
  </figure></div>
  <small>原论文图号与章节</small><aside>解释实验所支持的结论。</aside>
</section>
```

**公式。** 有 TeX Live 或 MiKTeX（含 latex、dvisvgm、preview、amsmath、amssymb）时，把每个公式作为 UTF-8 JSON 的一项，例如 `{"mean":"\\bar{x}=\\frac{1}{n}\\sum_{i=1}^n x_i"}`。键为输出文件名。运行 `python scripts/render_math.py equations.json media`，再用 `<img class="tex" src="{{asset:media/mean.svg}}" alt="样本均值" style="height:2.5em">` 插入。公式字号和邻近正文匹配，大公式单独成行。TeX 只编译自己核对过的表达式。也可以用本地 MathJax 或 KaTeX 的等效输出并嵌入字体。

**图与视频。** 用 PDF 渲染器导出真实首页与高分辨率裁图。保留原图裁剪坐标和图号，以便返修。源视频可用 `<video controls muted playsinline preload="metadata" poster="{{asset:media/poster.jpg}}" src="{{asset:media/demo.mp4}}"></video>`。用 figcaption 写明组别、任务与作者项目页。双栏使用 `.duo` 并显式设定 grid-template-columns；并列面板可用 `.parallel`。表格用 `.t25`。

**组合标识。** 同济封面的深蓝区域采用[官网白版](https://www.tongji.edu.cn/images/logo.png)，正文采用[统一身份认证页蓝版](https://iam.tongji.edu.cn/idp/themes/default/images/logo.png?a=1)。下载对应原图，在每个 section 内直接放置 `<img class="institution-mark" src="{{asset:media/tongji-blue.png}}" alt="同济大学">`，封面换为白版路径。交付前逐页核对图片和标题的边界。

**分区与分步。** 静态图表、视频和并排对照仅用 `.region` 分区。流程使用 `data-step` 按文档中首次出现的顺序逐步累积高亮。空属性各表示独立一步，使用相同的非空值可将同一步的多个节点或公式一起点亮。标题、固定参考图和页脚放在步骤之外。首屏显示淡化全貌，每前进一步点亮一组，前面各组持续高亮；回退依次撤销。视频由模板在进入所在页时统一启动。

```html
<div class="parallel">
  <div class="region" data-step><h3>前向扰动</h3><p>对训练动作加入已知噪声，构造指定时刻的输入。</p></div>
  <div class="region" data-step><h3>速度回归</h3><p>给定该输入和时刻，预测速度并与训练目标比较。</p></div>
</div>
```

**打包。** 将 section 片段保存到 slides.html，所有素材路径相对于此文件。运行 `python scripts/build.py slides.html talk.html --title "汇报题名"`。工具把明确标记的文件转成 data URI；正文由作者负责，避免插入外部 iframe、脚本和样式。只需 Python 3.9+ 标准库即可打包。

**放映检查。** 在 Chromium 中离线打开 talk.html，方向键翻页，F 全屏，N 开讲稿，G 开目录，Esc 关闭弹层，点原图放大。逐页截取相同尺寸（例如 1280×720）的画面，用 Pillow 等工具拼成全览。核对实际页数、隐藏的讲稿、公式渲染、页面边界及视频播放进度。最后交付真正验证过的文件。
