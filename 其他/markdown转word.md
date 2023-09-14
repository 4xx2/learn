---
title: "习惯"
author: 约翰·多伊
date: 2005年3月22日
output:
    word_document:
        path: Habits.docx
---
# 下载pandoc
Pandoc 是一个开源的文档转换工具，用于将一个文档格式转换成另一个文档格式。它可以将各种不同的文档格式之间进行转换，包括但不限于：
1. 标记语言转换：可以将Markdown、HTML、LaTeX、reStructuredText等标记语言互相转换。
2. 文档格式转换：可以将文本文档转换成PDF、Microsoft Word文档、ePub电子书等格式。
3. 特定领域的格式转换：可以用于将一些特定领域的文档格式进行转换，比如将电子表格格式转换成Markdown表格。

Pandoc 支持众多输入和输出格式，因此它在处理文档转换任务时非常强大和灵活。它是一个`命令行工具`，可以在各种操作系统上运行，包括Linux、macOS和Windows。

下载地址：[github下载](https://github.com/jgm/pandoc/releases)
选择正确的系统版本。我下载了window——msi格式安装包。
MSI 格式指代Windows 操作系统中的一种安装包文件格式，通常用于安装、升级和卸载Windows应用程序。MSI 文件包含了应用程序的安装信息、文件和注册表设置等。

# 在vscode上安装Markdown Preview Enhanced
- 搜索并安装插件即可；
- 转换前需要在markdown文件开头写说明；具体可查阅[MPE文档说明](https://shd101wyy.github.io/markdown-preview-enhanced/#/prince)
- 在预览界面右键点击Pandoc即可转换。

# MPE
例如：
```yaml
---
title: "习惯"
author: 约翰·多伊
date: 2005年3月22日
output:
  word_document:
    path: /Exports/Habits.pdf  #输出路径，默认当前
    toc: true  # 添加目录
    toc_depth: 2  # 目录深度，默认3
    number_sections: true  # 添加章节编号
    reference_docx: mystyles.docx  # 在生成 docx 文件时，使用指定的文件作为样式参考。# 没有则使用默认值
    highlight: tango  # 语法高亮，支持的样式包括 "default"、"tango"、"pygments"、"kate"、"monochrome"、"espresso"、"zenburn" 和 "haddock"（指定为 null 可以阻止语法高亮）

# LateX选项
fontsize: 11pt  # 字体大小
geometry: margin=1in  # geometry 类的选项（例如 margin=1in）；可重复
---
```

> yaml是配置文件的格式。

```yaml
---
export_on_save:  # 保存时导出
  markdown: true
---
```
