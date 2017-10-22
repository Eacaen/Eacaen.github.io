---
layout: post
title: " Pygame Notebook 2"
tagline: " Pygame Notebook 2"
categories: Python
author: "Hu Tianyun"
meta: "Springfield"
---

# 《Making Games with Python and Pygame》

*********************************************

## Notebook <2>
第五章的游戏 Simulate，让人去记住并重复游戏中图案显示的顺序， 主体还是画出矩形并能和鼠标键盘交互，在此之上增加了点击矩形时的音乐，一些类似特效的光影闪烁效果和实现显示的记分牌。

### 一般的逻辑顺序

1. 导入模块，设置全局变量，常量。
2. 设置界面，局部变量
	1. 文字 Surface 字体，大小，位置。
	2. 按键的颜色，大小，位置。
3. While 循环 **【在循环检测 QUIT 事件，否则是死循环无法退出】**
	1. 在循环中检测按键光标事件，检测碰撞。
	2. 循环中不断重新绘制全局和局部的 Surface。
	
### 亮点 / 思路
 * 所绘制的图标与图标占用的方块仅仅是大小相同，其他并没有什么联系。所以图标重新绘制和光标的碰撞到方块的检测并不矛盾和冲突，相反我觉得这是一种很好的思路和编写方式。
```
# 绘制 rect vs rect 检测
draw_rect( )
pygame.Rect( )
# 重复绘制图标
drawButtons()
```

 * 其实在前两章和本章的源码的循环中都有用背景色覆盖所有，然后再重新绘制文字，图标的部分，在搞清能这样的原因后，这样做的好处我觉得也有这样几条：
```
编写逻辑更加简单粗暴了，更新界面实际上就是整体重新绘制，不是界面的小修小补。
方便在界面上显示需要更新的文字【这里应该也可以小修小补的】，或是实时变更的分数等消息。
```
 * 功能
```Python
#让 Surface 显示出现在屏幕上
pygame.display.update()
# 确保动画不会像计算机绘制那样快的播放，调用 tick() 增加暂停，FPS 越小越慢
FPSCLOCK.tick(FPS)
```

### 播放音乐
 *  [音乐文件](/assets/files/beep1.ogg)

```Python
# -*- coding: utf-8 -*-

import pygame,sys
from pygame.locals import *
import time
WINDOWWIDTH = 640
WINDOWHEIGHT = 480

global FPSCLOCK, DISPLAYSURF, BEEP1
pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

pygame.display.set_caption('Play Sound')
BEEP1 = pygame.mixer.Sound('beep1.ogg')

while True:
	for event in pygame.event.get(): # event handling loop
		if event.type == MOUSEBUTTONUP:
			mousex, mousey = event.pos
			BEEP1.play()

		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
```
### 颜色效果的制作

 *  通过不断更改透明度 alpha 实现颜色的明暗变化效果。

> 调用 convert_alpha() 方法，以便该 Surface 对象能够具有一个绘制于期上的透明色，否则的话将会忽略 Color 对象的 alpha 值并自动保存为 255。

```Python
# -*- coding: utf-8 -*-

import pygame,sys,random
from pygame.locals import *
import time
FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480

#	R	G	B
WHITE	= (255, 255, 255)
BLACK	= (  0,   0,   0)

bgColor = BLACK

def changeBackgroundAnimation(animationSpeed=5):
	global bgColor
	newBgColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

	newBgSurf = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT))
	newBgSurf = newBgSurf.convert_alpha()
	r, g, b = newBgColor
	for alpha in range(0, 255, animationSpeed): # animation loop
		DISPLAYSURF.fill(bgColor)

		newBgSurf.fill((r, g, b, alpha))
		DISPLAYSURF.blit(newBgSurf, (0, 0))

		pygame.display.update()
		FPSCLOCK.tick(FPS)
	bgColor = newBgColor

def main():
	global FPSCLOCK, DISPLAYSURF
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	pygame.display.set_caption('Color')

	while True:
		for event in pygame.event.get(): # event handling loop
			if event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				changeBackgroundAnimation()
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
				
		pygame.display.update()

if __name__ == '__main__':
	main()
```

