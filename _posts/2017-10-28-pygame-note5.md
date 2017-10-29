---
layout: post
title: " Pygame Notebook 5 大鱼吃小鱼"
tagline: " Pygame Notebook 5"
categories: Python
author: "Hu Tianyun"
meta: "Springfield"
---

# 《Making Games with Python and Pygame》

*********************************************

## Notebook <5>
第八章的游戏 Squrrile 大鱼吃小鱼。本次游戏从代码量上看来比俄罗斯方块少了不少，但是游戏界面看上去比较像模像样了。
背景会随着方向的移动而变化，松鼠也会跳跃着移动。屏幕上也有其他移动方向和大小随机的松鼠。有了血条显示松鼠的生命值。死亡后界面上仍有松鼠移动，当松鼠变到很大时会有提示；生命值结束一段时间后自动重新开始。

第八章的游戏看上去更加漂亮和丰富。

### 亮点 / 思路
 *  松鼠属性的字典表示，更加直观专业。
 *  相机视角造成了一种窗口移动的效果。
 *  受伤后的闪烁，无敌状态。
 *  动画效果仍然是每次重新绘制所有。
 *  有效界面的判断，界面外生成物体形成突然进入的效果。


### 松鼠的表示
 *  使用字典存储了所有的属性。

```Python
playerObj = {'surface': pygame.transform.scale(L_SQUIR_IMG, (STARTSIZE, STARTSIZE)),
	'facing': LEFT,
	'size': STARTSIZE,
	'x': HALF_WINWIDTH,
	'y': HALF_WINHEIGHT,
	'bounce':0,
	'health': MAXHEALTH}
```

### 视角的移动，相机的延迟
 *  相机所能看到的区域叫做相机视图，camera view，其中心位于游戏坐标的一点。由于相机看到的内容显示于玩家的屏幕上，相机坐标与像素坐标是相同的。要得到松鼠的像素坐标，即松鼠出现在屏幕上的位置，用松鼠的游戏坐标减去相机的原点坐标。
 *  松鼠的移动实际上是松鼠与其他物体相对未知的移动，是基于相机坐标的移动上的相对移动。通过松鼠在界面上的位置，计算出一个“所谓”的相机坐标，将松鼠向左移动，另外**物体的坐标减去相机坐标**则会向相反的方向移动，而界面大小是一定的，造成移动效果。
 *  但是这样做，通过例子的观察看出，这样移动的坐标系与全局的坐标系或是界面的坐标系没有什么必然关联。若是在界面上提前定义好一个坐标确定的方块，方块将不随界面的”移动“。
 *  [运行文件]({{ site.url }}/assets/files/Pygame_book/my_camera_pos.py)  


### 松鼠的跳跃
 *  使用正弦函数值加载到 Y 坐标。


### 闪烁效果
 *  画一次，覆盖，再画一次，覆盖，重复的视觉暂留效果。
 *  通过时间取余数来判断是否覆盖重画。
 *  [运行文件]({{ site.url }}/assets/files/Pygame_book/my_load_img.py)  
 
```Python
# flashIsOn is 1 or 0
flashIsOn = round(time.time(), 1) * 10 % 2 == 1
# 巧妙的逻辑判断
if not gameOverMode and not (invulnerableMode and flashIsOn):
	playerObj['rect'] = pygame.Rect( (playerObj['x'] - camerax, playerObj['y'] - cameray -
	getBounceAmount(playerObj['bounce'], BOUNCERATE, BOUNCEHEIGHT),
	playerObj['size'],playerObj['size']) )

	DISPLAYSURF.blit(playerObj['surface'], playerObj['rect'])
```


## 函数用法
 *  设置窗口标题栏图标，理想大小 32*32像素。
 
```Python
pygame.display.set_icon(pygame.image.load('gameicon.png'))
```

 *  加载图像，反转图像。
 *  循环加载图像。
 
```Python
L_SQUIR_IMG = pygame.image.load('squirrel.png')
R_SQUIR_IMG = pygame.transform.flip(L_SQUIR_IMG, True, False)

for i in range(1, 5):
	GRASSIMAGES.append(pygame.image.load('grass%s.png' % i))
```

 *  设置窗口标题栏图标，理想大小 32*32像素。
 
```Python
pygame.display.set_icon(pygame.image.load('gameicon.png'))
```

 *  反向遍历列表删除元素，不会报错。
 
```Python
for i in range(len(LIST)-1, -1, -1):
	del xxx
```