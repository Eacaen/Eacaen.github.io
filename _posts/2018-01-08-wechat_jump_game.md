---
layout: post
title: "开挂玩微信跳一跳"
tagline: "wechat jump game"
categories: Python
author: "Hu Tianyun"
meta: "Springfield"
subtitle:  <h4>Download
            <a role="button" class="btn btn-primary hvr-grow-shadow" href="https://github.com/Eacaen/wechat_jump_game" target="_blanks">
                <span class="octicon octicon-mark-github"></span> GitHub
            </a>
            </h4>
            <h4> </h4>
---

# 开挂玩微信跳一跳
[程序地址](https://github.com/Eacaen/wechat_jump_game)

[B站视频-->酸爽。跳一跳20倍播放从4000分到20000＋](https://www.bilibili.com/video/av18307956)

<iframe src="//player.bilibili.com/player.html?aid=18307956&cid=29885527&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>

换了小米mix2后发现安卓真是各种权限开放。网上也有各种微信跳一跳的自动挂，尝试一下做个记录。

##  获取安卓USB调试权限
 * ubuntu 安装abd tool 调试安卓，需要有java8，如果和已有的java７冲突，可参考网上教程，教程亲测可用。
 *  小米打开开发者模式，开启USB调试，开启允许模拟触屏。
 *  shell 中打开adb device 可以发现设备，如果发现不了，网上教程亲测可用。


## 手动模式
文件中手动模式，使用matplotlib库，将屏幕截图作为动画的部分，鼠标选择起跳和结束位置，乘上起跳系数后使用adb发送按压时间完成跳跃．
 * 速度慢，依赖鼠标点击精度。
 * 方法很好，直观且可以学习很多新的方法

## 自动模式
### 使用OpenCV
进行图像处理，截图中心部分。高斯去噪后找到图像边缘，继而找出小人的中心和下一个跳板的中心。
 * 每次跳到中心后，会在下个位子中心显示白点，可以直接寻找，更加方便

### 使用Tensorflow
使用了800--1000张图片,截取中心部分，灰度显示，利用卷积神经网络，使用 *使用OpenCV* 找到的中心作为输入，按压时间作为训练结果。训练效果有些许，但是不好
 * 学艺不精，参数调试，层数选择有待学习

## DEBUG
 * 对于不是正方形的跳板，目前只能放弃，但是不影响
 * 深度学习并没有学习到我想象中效果，渣渣电脑和渣渣技术


********************************************
又要多多学习一个了。

 > [参考github@wangshub](https://github.com/wangshub/wechat_jump_game)
