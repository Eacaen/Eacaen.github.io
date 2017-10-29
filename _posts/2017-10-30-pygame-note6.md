---
layout: post
title: " Pygame Notebook 6 推箱子"
tagline: " Pygame Notebook 6 "
categories: Python
author: "Hu Tianyun"
meta: "Springfield"
---

# 《Making Games with Python and Pygame》

*********************************************

## Notebook <6> 推箱子
第九章的游戏 Star Pusher 经典的推箱子游戏。背景比松鼠游戏更加绚丽，物体也更加多样，虽然看上去都是贴图。人物推星星时星星的移动，一格一格。推到角落就不能在推了。推到了指定位置就进入下一关，通过读取关卡文件进行游戏地图绘制。

第十章的介绍了几个更加复杂的游戏，代码量更多更庞杂。以后慢慢细看吧。

### 亮点 / 思路
 *  复杂广泛的背景贴图，关卡文件的意义。
 *  胜负的判断。
 *  能不能移动的判断。


### 去除关卡文件中的注释行
 *  读取文件，删除 '；'开始的行。

```Python
line.find(';') #找到；开始的行，返回第一个 ； 的index = 0
line = line[:line.find(';')] #line 为空
```
### 待续。。。

## 监听鼠标事件
 *  event.type 中的 MOUSEBUTTONUP 和 MOUSEBUTTONDOWN 包含了按动/松开 左键（1），滚轮（2），右键（3），上滚（4），下滚（5）的事件。

```Python
for event in pygame.event.get(): # event handling loop
	if event.type == MOUSEBUTTONUP:
		if event.button == 1 or event.button ==4:
			# do something
		if event.button == 3 or event.button ==5:
			# do something
```