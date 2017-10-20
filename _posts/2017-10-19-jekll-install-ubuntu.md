---
layout: post
title: " Jekyll install in Ubuntu"
tagline: "jekyll install questions and solutions in Ubuntu"
categories: Ubuntu
author: "Hu Tianyun"
meta: "Springfield"
---
## jekyll install in Ubuntu

### Ubuntu 安装 jekyll 时遇到的一些问题。
 

* 开始时 使用命令

		ruby -v	

会发现 Ubuntu 中竟然有一个 ruby1.8，许多网站都说 Ubuntu 中是不自带 ruby 的。但是这个 ruby 貌似没什么用，jekyll 基本都要 ruby > 1.9 或是 >2.0 。

* 安装缓慢，改变安装源

		gem sources --add https://gems.ruby-china.org/ --remove https://rubygems.org/
		gem sources -l 查看源
确保源里面只有 https://gems.ruby-china.org/ 

* 使用 jekyll serve 遇到一些像 GitHub 权限等问题，使用

		bundle exec jekyll serve

* 编译全局，会将所有的内容放到 _site 中

		jekyll build
		bundle exec jekyll build

### Theme 下载后使用的一些问题

* 一开始使用一些模板时会出现一堆的错误，慢慢看错误，Google就行，基本都能找到答案。两个包可以安装下

		gem install minima 
		gem install jekyll-feed

* **注意** 修改文字，添加图片预览时的 网页地址，最好将_config.yml 中的 原始网页先注释掉，不然会联网回到 github 里保存的而不是修改完成的。
* xxx.md 与 xxx.html 在编辑时是同步更新的，不需要 build 后再启动 serve。

* include/ 里面使用的 HTML bootstrap 语言，一些相关的布局语法可以Google。