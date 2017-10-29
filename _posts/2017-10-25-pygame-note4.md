---
layout: post
title: " Pygame Notebook 4 俄罗斯方块"
tagline: " Pygame Notebook 4"
categories: Python
author: "Hu Tianyun"
meta: "Springfield"
---

# 《Making Games with Python and Pygame》

*********************************************

## Notebook <4>
第七章的游戏 Tetromino 俄罗斯方块。背景区域的划分规划，背景音乐的播放。砖块的构造，下落，旋转，消失。砖块碰撞叠加的判断，游戏结束的判断。代码量接近前两章的两倍多，编写更加复杂了。

### 亮点 / 思路
 *  游戏板数据结构
 > 游戏板数据结构是用来记录之前着陆的砖块占据了哪些矩形空格的一种数据表示。当前下落的砖块在游戏板数据结构中并没有标记。
 *  砖块的表示使用的是列表的列表，区分了 fallingOiece 和 nextPiece 。使用砖块用字典表示了，从界面的中点下降。
 *  砖块的旋转是直接将砖块旋转的顺序按照列表的排列写进了砖块的表示中去了，直接查表不用计算了。
 *  后台程序中给所有的界面方块赋予了一个 BLANK 值用于检测是否需要画上砖块。
 *  砖块下降动画的制作仍然是重新绘制所有了。
 *  砖块下降到何处就不能下降了，如何判断，如何加到游戏板数据结构中去？
 > 通过isValidPosition() 判断砖块是否处于有效位置，如果返回 False 则说明砖块当前需要判断的位置无效
 *  用程序运行间隔的时间来控制砖块下降的速度，通过调节阀值进行关卡的增加。
 *  游戏结束的标准：下降砖块没有足够的放置空间，如何判断。
 *  暂停事件按键抬起才触发，移动按下就触发，抬起才结束，可以一直移动不用按个不停。检测按键松开来判断玩家是否想要继续移动砖块，便于检查长按的情况。


### keyDown keyPress keyUp  事件的区别
 *  [事件区别](http://blog.sina.com.cn/s/blog_a401a1ea0101edah.html "事件的区别")
 *  按键弹起才触发，按键按下就触发的区别就在这里。

```Python
# 等待按键弹起？？？
def checkForKeyPress():
	# Go through event queue looking for a KEYUP event.
	# Grab KEYDOWN events to remove them from the event queue.
	checkForQuit()

	for event in pygame.event.get([KEYDOWN, KEYUP]):
		if event.type == KEYDOWN:
			continue
		return event.key
	return None
```

### 背景音乐一直播放
 *  使用 pygame.mixer.music。

```Python
pygame.mixer.music.load('xxx')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.stop()
```

### 砖块的表示和调用
 *  S_SHAPE_TEMPLATE 表示砖块及其可能的旋转表示，列表的列表。
 *  PIECE 砖块组成的字典。
 *  调用砖块时，又把砖块作为 piece 字典中的一个 value 值并增加其他的属性。
 
```Python
PIECES = {'S': S_SHAPE_TEMPLATE, 'Z': Z_SHAPE_TEMPLATE, 'J': J_SHAPE_TEMPLATE, 'L': L_SHAPE_TEMPLATE,
	     'I': I_SHAPE_TEMPLATE,'O': O_SHAPE_TEMPLATE, 'T': T_SHAPE_TEMPLATE}
def getNewPiece():
	# return a random new piece in a random rotation and color
	shape = random.choice(list(PIECES.keys()))
	newPiece = {'shape': shape,
			'rotation': random.randint(0, len(PIECES[shape]) - 1),
			'x': int(BOARDWIDTH / 2) - int(TEMPLATEWIDTH / 2),
			'y': -2, # start it above the board (i.e. less than 0)
			'color': random.randint(0, len(COLORS)-1)}
```


### 判断砖块需要处于的位置是否有效 

**A smart function**

 *  board 为游戏板数据结构，piece 为砖块位置，通过adjX,Y 调节从而判断砖块将要处于的位置是否有效。
 
```Python
def isValidPosition(board, piece, adjX=0, adjY=0):
	# Return True if the piece is within the board and not colliding
	for x in range(TEMPLATEWIDTH):
		for y in range(TEMPLATEHEIGHT):
			#检测游戏板之外的方块
			isAboveBoard = y + piece['y'] + adjY < 0 
			if isAboveBoard or PIECES[piece['shape']][piece['rotation']][y][x] == BLANK:
				continue
			#检测砖块是否在游戏板上
			if not isOnBoard(x + piece['x'] + adjX, y + piece['y'] + adjY):
				return False
			#检测砖块的方块所在的游戏板空格不为空白
			#砖块上的空白和在检测时和游戏板上的空白检测并不冲突
			if board[x + piece['x'] + adjX][y + piece['y'] + adjY] != BLANK:
				return False
	return True

```

### 判断砖块是否到底【或】到不能再向下的位置

 *  仍然通过isValidPosition() 函数提前一格判断位置是否有效，如果无效了（到底了或是有阻挡），说明当前位置就是下落的最低位置，将砖块数据放入游戏板数据结构中，加分计算等级；如果是有效位置，就可以继续下降。
 
![ValidPosition](/post_img/tetromino1.png  "ValidPosition")

```Python
if time.time() - lastFallTime > fallFreq:
	# see if the piece has landed
	if not isValidPosition(board, fallingPiece, adjY=1):
		# falling piece has landed, set it on the board
		addToBoard(board, fallingPiece)
		score += removeCompleteLines(board)
		level, fallFreq = calculateLevelAndFallFreq(score)
		fallingPiece = None
	else:
		# piece did not land, just move the piece down
		fallingPiece['y'] += 1
		lastFallTime = time.time()
```

### 检查，删除和填满一行

 *  判断所在行的空格是否存在 BLANK。
 *  倒序检测所有行，如有一行填满，则将该行以上所有的内容向下复制赋值一遍，第 0 行填充 BLANK，此时 y 值不变，继续判断循环【方便了多行填满的情况】；没有则 y + 1。

### 游戏结束的判断
 *  仍然是isValidPosition() 函数。直接在旧砖块落底，新砖块初始落下时判断，如果一开始就没有足够空间，说明游戏结束了。

## 函数复习
 > 在调用绘制函数以便让显示 Surface 对象看上去是你想要的方式之后，必须调用 update 让 显示 Surface 真正出现在用户显示器上。
```Python
pygame.display.update()
```