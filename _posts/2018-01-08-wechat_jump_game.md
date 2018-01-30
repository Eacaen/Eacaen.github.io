---
layout: post
title: "开挂玩微信跳一跳"
tagline: "wechat jump game"
categories: Python
author: "Hu Tianyun"
meta: "Springfield"
---

[参考github@wangshub](https://github.com/wangshub/wechat_jump_game)

换了小米mix2后发现安卓真是各种权限开放。网上也有各种微信跳一跳的自动挂，尝试一下做个记录。

##  获取安卓USB调试权限
 * ubuntu 安装abd tool 调试安卓，需要有java8，如果和已有的java７冲突，网上教程亲测可用。
 *  小米打开开发者模式，开启ＵＳＢ调试，开启允许模拟触屏。
 *  adb device 可以发现设备，如果发现不了，网上教程亲测可用。


## 手动模式
文件中手动模式，使用matplotlib库，将屏幕截图作为动画的部分，鼠标选择起跳和结束位置，乘上起跳系数后使用adb发送。

## 自动模式
图像处理，找出小人的中心和下一个跳板的中心。

又要多多学习一个了。

