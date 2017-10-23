---
layout: post
title: " Pygame Notebook 3"
tagline: " Pygame Notebook 3"
categories: Python
author: "Hu Tianyun"
meta: "Springfield"
---

# 《Making Games with Python and Pygame》

*********************************************

## Notebook <3>
第六章的游戏 Wormy 贪吃蛇游戏， 开局显示旋转变化的字体和方块，按下任意按键后会显示游戏界面，划分的网格，游走的蛇（绿色方块），苹果（红色的方块），碰撞到苹果身体变长，碰撞到自己和墙壁游戏结束，暂停并显示 Game Over，按下任意按键后又再次重新开始。同时实时显示分数。

### 亮点 / 思路
 * 程序很好的结合了吃苹果和游动的处理，使用蛇头坐标，一个字典列表表示蛇，每次都删除末尾，吃到则不删除。
 * Game Over时，进入显示Game Over while 死循环等待退出，其间其他的显示部分暂停在原处，死循环阻塞住了其他显示程序，显示程序仍旧在 Surface 上面显示界面，造成一种另外有暂停程序的假象。
 * 字体背景会随着字体的变化而变化，不需要额外控制。
 *  2D 图像的旋转，不完美，不应该直接覆盖变量，复用变量名的话则会造成字体的 Surface 越来越大，报错。
 *  智能的退出函数。

### 蛇的表示和长度的增加
 *  在当前的前进方向上增加头，删去尾巴，每次重新绘图时感觉就是在前进；吃到苹果则不删去，感觉就是增加了长度。

```Python
wormCoords = [ {'x':startx , 'y': starty} ,  {'x':startx-1 , 'y': starty}  ,  {'x':startx-2 , 'y': starty} ,{'x':startx-3 , 'y': starty} ]
if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
	apple = getRandomLocation() # set a new apple somewhere
else:
	del wormCoords[-1] 

if direction == UP:
	newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
elif direction == DOWN:
	newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1}
elif direction == LEFT:
	newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']}
elif direction == RIGHT:
	newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']}

wormCoords.insert(0, newHead)

```

### 显示 pygame.event 中的 type 值
 *  [运行文件]({{ site.url }}/assets/files/Pygame_book/my_event_test.py)  

```Python
#/usr/bin/env python
#coding=utf8

import random, pygame, sys
from pygame.locals import *

WINDOWWIDTH = 640
WINDOWHEIGHT = 480

def main():
	pygame.init()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	pygame.display.set_caption('event test')


	while True:
for event in pygame.event.get():
	print 'event.type' , event.type

	if event.type == QUIT:
pygame.quit()
sys.exit()
	elif event.type == KEYDOWN:
print event.key 


if __name__ == '__main__':
	main()
```

### 显示 文字旋转，背景转化，网格划分，按键退出
 *  [运行文件]({{ site.url }}/assets/files/Pygame_book/my_wormy_test.py) 
 *  背景转化更好的说明了每次用背景色覆盖后重新绘图的原理和好处
 *  文字旋转
 > pygame.transform.rotate( surface , rotate_angle) 并不会改变传递给它的 Surface 对象，而是返回一个新的Surface 对象，旋转后的图形绘制于新的 Surface 对象上。
 
 所以每次都重新绘图。

 *  旋转不要复用变量名。
 > pygame.error: Width or height is too large
 *  退出函数 checkForKeyPress() 的使用
 *  网格划分，循环划线。
```Python
#/usr/bin/env python
#coding=utf8

import random, pygame, sys
from pygame.locals import *

FPS = 5
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

#			 R	G	B
WHITE	 = (255, 255, 255)
BLACK	 = (  0,   0,   0)
RED	   = (255,   0,   0)
GREEN	 = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
BGCOLOR = BLACK

def terminate():
	pygame.quit()
	sys.exit()

def main():
	global FPSCLOCK, DISPLAYSURF, BASICFONT

	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
	pygame.display.set_caption('Wormy')

	degrees1 = 0
	degrees2 = 0

	while True:
		
		showStartScreen()
		showGameOverScreen()

	print 'exit'

def drawGrid():
	for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
		pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
	for y in range(0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
		pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))
def drawPressKeyMsg():
	pressKeySurf = BASICFONT.render('Press a key to play.', True, DARKGRAY)
	pressKeyRect = pressKeySurf.get_rect()
	pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
	DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

def checkForKeyPress():
	if len(pygame.event.get(QUIT)) > 0:
		terminate()

	keyUpEvents = pygame.event.get(KEYUP)
	if len(keyUpEvents) == 0:
		return None
	if keyUpEvents[0].key == K_ESCAPE:
		terminate()
	return keyUpEvents[0].key

def showStartScreen():
	titleFont = pygame.font.Font('freesansbold.ttf', 100)
	titleSurf1 = titleFont.render('Wormy!', True, WHITE, DARKGREEN)
	titleSurf2 = titleFont.render('Wormy!', True, GREEN)

	degrees1 = 0
	degrees2 = 0
	while True:

		# DISPLAYSURF.fill(BGCOLOR)
		rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1) #返回的是新的 Surface 对象
		rotatedRect1 = rotatedSurf1.get_rect()
		rotatedRect1.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
		DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)

		rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2) 
		rotatedRect2 = rotatedSurf2.get_rect()
		rotatedRect2.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
		DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)

		# for event in pygame.event.get():
		# 	if event.type == QUIT:
		# 		terminate()

		if checkForKeyPress():
			pygame.event.get() # clear event queue
			return
		drawPressKeyMsg()
		drawGrid()
		pygame.display.update()
		FPSCLOCK.tick(FPS)
		degrees1 += 3 # rotate by 3 degrees each frame
		degrees2 += 7 # rotate by 7 degrees each frame

def showGameOverScreen():
	gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
	gameSurf = gameOverFont.render('Game', True, WHITE)
	overSurf = gameOverFont.render('Over', True, WHITE)
	gameRect = gameSurf.get_rect()
	overRect = overSurf.get_rect()
	gameRect.midtop = (WINDOWWIDTH / 2, 10)
	overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)

	DISPLAYSURF.blit(gameSurf, gameRect)
	DISPLAYSURF.blit(overSurf, overRect)

	drawPressKeyMsg()

	pygame.display.update()
	pygame.time.wait(500)
	checkForKeyPress() # clear out any key presses in the event queue

	while True:
		if checkForKeyPress():
			pygame.event.get() # clear event queue
			return

if __name__ == '__main__':
	main()
```