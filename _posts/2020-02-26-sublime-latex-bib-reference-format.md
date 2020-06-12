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
#######################################################################
\newdimen\bibindent
\setlength\bibindent{1.5em}
\newdimen\bibspacing
\setlength\bibspacing\z@
\renewenvironment{thebibliography}[1]{%
\section*{\refname
\@mkboth{\MakeUppercase\refname}{\MakeUppercase\refname}}%
\list{\@biblabel{\@arabic\c@enumiv}}%
{\settowidth\labelwidth{\@biblabel{#1}}%
\leftmargin\labelwidth
\advance\leftmargin\labelsep 
\itemsep\z@skip % should this be commented out?
\parsep\z@skip % should this be commented out?
\@openbib@code
\usecounter{enumiv}%
\let\p@enumiv\@empty
\renewcommand\theenumiv{\@arabic\c@enumiv}}%
\sloppy\clubpenalty4000\widowpenalty4000%
\sfcode`\.\@m}
{\def\@noitemerr
{\@latex@warning{Empty `thebibliography' environment}}%
\endlist}
#######################################################################