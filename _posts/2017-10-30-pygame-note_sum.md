---
layout: post
title: " Pygame Notebook 7 总结"
tagline: " Pygame Notebook 7 "
categories: Python
author: "Hu Tianyun"
meta: "Springfield"
---

# 《Making Games with Python and Pygame》

*********************************************

## Notebook <7> Summary
经过近一周的阅读学习，这本书上前面几章的代码和内容大致就到这了。剩下的实在太长且重复了之前的一些内容，游戏的规则也渐渐复杂起来，留待以后慢慢研习。
至此关于 Pygame 中的一些基本函数和常用操作都差不多了解不少，现将前几章中代码中比较有技巧，有意思的部分复习整理一下留做记录。

### 演示第二三四章中方块变化的效果
 *  [运行文件]({{ site.url }}/assets/files/Pygame_book/my_puzzleSlide_test.py)  
 *  小程序演示了方块的遮盖，还原。方块透明度的变化，通过贪吃蛇演示了动画制作的原理。
 *  其中贪吃蛇和方块变化的 FPS 需要设置成不一样。
 *  演示了鼠标各个按键滚轮的信号监听，键盘的信号监听。

![演示图](/post_img/puzzle_slide.png  "演示图")

### 第十章中翻转棋子的游戏是如何让检测棋子翻转的呢？
 *  巧妙的通过列表循环直接循环了棋子周围的8个方向并在循环中不断跟进查找直到终止本次跟进，找出不同的棋子放进待翻转的列表，最后在一起重新绘制。


```Python
	for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
		x, y = xstart, ystart
		x += xdirection
		y += ydirection
		if isOnBoard(x, y) and board[x][y] == otherTile:
			# The piece belongs to the other player next to our piece.
			x += xdirection
			y += ydirection
			if not isOnBoard(x, y):
				continue
			while board[x][y] == otherTile:
				x += xdirection
				y += ydirection
				if not isOnBoard(x, y):
					break # break out of while loop, continue in for loop
			if not isOnBoard(x, y):
				continue
			if board[x][y] == tile:
				# There are pieces to flip over. Go in the reverse
				# direction until we reach the original space, noting all
				# the tiles along the way.
				while True:
					x -= xdirection
					y -= ydirection
					if x == xstart and y == ystart:
						break
					tilesToFlip.append([x, y])
```
 
### 第十一章中检测到不同颜色边沿和局部颜色闪烁是如何实现的呢？
 *  [演示文件]({{ site.url }}/assets/files/Pygame_book/my_puzzlePartFlash_test.py)  
 *  先递归调用漫水算法找到不一致的方块，由于将列表作为了**函数参数**且没有复制，在函数调用过程中直接被修改了内部的变量，该列表作为全局画图参数这样非但不影响，反而隐藏了一些潜在BUG，貌似有助于编程。
 *  局部闪烁的原因是：即使在原来的颜色上闪烁人眼也不能察觉出来，如果在闪烁函数中加入一个全局的 DISPLAYSURF.fill(WHITE) 那么就可以就看出来其实是每个颜色都闪了。
 *  演示中加入了实时显示鼠标位置的部分。

### 待续
 *  一些音乐播放，图片加载，背景闪烁，背景贴图效果可以看前面的几节内容。
