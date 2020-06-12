---
layout: post
title: " Latex Sublime 参考文献格式问题 "
tagline: "Latex Notebook"
categories: Latex
author: "Hu Tianyun"
meta: "Springfield"
---

解决论文中latex格式下参考文献的条目间距过大问题

## 参考：
	http://blog.sina.com.cn/s/blog_5e16f1770100ldv5.html
	https://www.jianshu.com/p/4c10427d0c34
	http://dcwww.camd.dtu.dk/~schiotz/comp/LatexTips/LatexTips.html

## 下载并添加.sty 文件至latex目录中

### 重点在于\section*{\refname
 *  \renewcommand{\bibname}{参考文献}
 *  \renewcommand\refname{参考文献}
 *  修改section* 或是其他的标题，可以更改显示格式

附上 bibspacing.sty 内容



