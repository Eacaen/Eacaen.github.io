---
layout: post
title: " Pygame Notebook 1"
tagline: " Pygame Notebook 1"
categories: Python
author: "Hu Tianyun"
meta: "Springfield"
---

# 《Making Games with Python and Pygame》

*********************************************

## Notebook <1>
在半敲半复制了第三章 Memory Puzzle 和第四章 Slide Puzzle 的源码之后，结合前两章节所讲的东西算是对如何使用 Pygame 编写一个带有界面和操作的小游戏有了基本的认识和了解。这两章的代码主要功能都是在 原始的 Surface 上面绘制带有颜色和文字内容的矩形块，并能对鼠标键盘等操作进行响应。抛开其中简单的数学图形计算不谈，先把其中 Pygame 编写的思路和 API 的调用方式记录下。

### Memory Puzzle & Slide Puzzle 
#### 像素坐标系和矩形坐标系的转化
 * 两个源码都始终用的是矩形左上角的像素坐标值进行选择和计算 
 
```Python
def leftTopCoordsOfBox(boxx , boxy):
	# Convert board coordinates to pixel coordinates
	left = boxx * (BOXSIZE + GAPSIZE ) + XMARGIN
	top  = boxy * (BOXSIZE + GAPSIZE ) + YMARGIN
	return (left , top)

def getLeftTopOfTile(tileX, tileY):
	left = XMARGIN + (tileX * TILESIZE) + (tileX - 1)
	top = YMARGIN + (tileY * TILESIZE) + (tileY - 1)
	return (left, top)
```

#### 获取光标像素位置，获取键盘值

 * 获取光标像素位置，检查光标位于哪一个方块上

```Python
for event in pygame.event.get():
	event.type == MOUSEMOTION:#or other types
		mousex , mousey = event.pos

# 遍历所有的矩形，检查鼠标与哪一个矩形碰撞了
# 返回矩形所在的行列值，注意坐标系的规定
def getSpotClicked(board, x, y):
    # from the x & y pixel coordinates, get the x & y board coordinates
	for tileX in range(len(board)):
		for tileY in range(len(board[0])):
			left, top = getLeftTopOfTile(tileX, tileY)
			tileRect = pygame.Rect(left, top, TILESIZE, TILESIZE)
			if tileRect.collidepoint(x, y):
				return (tileX, tileY)
	return (None, None)
```

 * 获取键盘值

```Python
for event in pygame.event.get():
	if event.type == KEYUP:
		if event.key in (K_LEFT, K_a) and isValidMove(mainBoard, LEFT):
			slideTo = LEFT
		elif event.key in (K_RIGHT, K_d) and isValidMove(mainBoard, RIGHT):
			slideTo = RIGHT
		elif event.key in (K_UP, K_w) and isValidMove(mainBoard, UP):
			slideTo = UP
		elif event.key in (K_DOWN, K_s) and isValidMove(mainBoard, DOWN):
			slideTo = DOWN 
```


 * 使用 assert 语句检查
 
```Python
assert (BOARDWIDTH * BOARDHEIGHT) %2 == 0
```
#### import random 
 * 截取列表前 numIconsUsed 个， 打乱列表
 
```Python
icons = icons[:numIconsUsed] * 2
random.shuffle(icons)
```

## Pygame 绘制思路
 * 导入模块
 
```Python
import pygame,sys
from pygame.locals import *
```
 * 启动，设置全部变量，窗口大小，标题，字体
 
```Python
global FPSCLOCK , DISPLAYSURF , BASICFONT
pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH , WINDOWHEIGHT))
pygame.display.set_caption('NAME')
BASICFONT = pygame.font.Font('freesansbold.ttf' , BASICFONTSIZE)

# 设置字体抗锯齿，颜色，背景颜色
def makeText(text, color, bgcolor, top, left):
	# create the Surface and Rect objects for some text.
	textSurf = BASICFONT.render(text, True, color, bgcolor) #返回的是字体的 Surface
	textRect = textSurf.get_rect()
	textRect.topleft = (top, left)
	return (textSurf, textRect)
```
 * 更新绘图，帧数
 
```Python
pygame.display.update()
FPSCLOCK.tick(FPS)
```
 * 在 Slide Puzzle 中通过不断地重设背景颜色，不断地**重复绘制**，层叠Surface整体  从而实现效果。
 * 矩形方块的打开覆盖，贴片的滑动是通过绘制大小不一的矩形图案实现的。
 
```Python
	drawBoard(board, message)  #每次都重新绘制整个图
	baseSurf = DISPLAYSURF.copy() # 深度拷贝
	# draw a blank space over the moving tile on the baseSurf Surface.
	moveLeft, moveTop = getLeftTopOfTile(movex, movey)
	pygame.draw.rect(baseSurf, BGCOLOR, (moveLeft, moveTop, TILESIZE, TILESIZE)) #用背景色方块替换原来的

	for i in range(0, TILESIZE, animationSpeed):
	# animate the tile sliding over
		checkForQuit()
		DISPLAYSURF.blit(baseSurf, (0, 0)) # 覆盖空白方块后继续画图，显示移动
		if direction == UP:
			drawTile(movex, movey, board[movex][movey], 0, -i)
		if direction == DOWN:
			drawTile(movex, movey, board[movex][movey], 0, i)
		if direction == LEFT:
			drawTile(movex, movey, board[movex][movey], -i, 0)
		if direction == RIGHT:
			drawTile(movex, movey, board[movex][movey], i, 0)
	
		pygame.display.update()
		FPSCLOCK.tick(FPS)
```
 * Start , Reset 等按键是通过检测相同位置的矩形范围是否与光标碰撞实现的。
 
```Python
#画矩形
pygame.draw.rect(baseSurf, BGCOLOR, (moveLeft, moveTop, TILESIZE, TILESIZE))
#利用矩形所在位置进行检测
boxRect = pygame.Rect(left , top , BOXSIZE , BOXSIZE)
if boxRect.collidepoint(event.pos):
	fun_def()
```