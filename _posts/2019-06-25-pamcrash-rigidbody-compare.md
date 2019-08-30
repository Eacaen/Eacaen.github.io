---
layout: post
title: " PAMCRASH 多刚体设置对比 "
tagline: "PAMCRASH Notebook"
categories: PAMCRASH
author: "Hu Tianyun"
meta: "Springfield"
---
**结果仅供交流，对计算结果的精确性不负任何责任**

> 结果<.gif-等待加载>

<img src="/post_img/PAM-RIGID-COMP/del-rigid_body_sp_test_001.gif" data-canonical-src="/post_img/PAM-RIGID-COMP/del-rigid_body_sp_test_001.gif" />

<img src="/post_img/PAM-RIGID-COMP/rigid_body_sp_test_001.gif" data-canonical-src="/post_img/PAM-RIGID-COMP/rigid_body_sp_test_001.gif" />

<img src="/post_img/PAM-RIGID-COMP/2-rigid_body_sp_test_001.gif" data-canonical-src="/post_img/PAM-RIGID-COMP/2-rigid_body_sp_test_001.gif" />

## 模型介绍
### 模型1
模型不设置刚体，给以两个独立的 soild part以一定的初速度。

<img src="/post_img/PAM-RIGID-COMP/del-rigid_body_sp_test_001.JPEG" data-canonical-src="/post_img/PAM-RIGID-COMP/del-rigid_body_sp_test_001.JPEG" />

### 模型2
* 将两个part放到同一个刚体中去，计算重心，将一定的初速度*加载至重心点上去*。
* 地板固支四条edge边。
* 设置其中一个part与地板接触。

<img src="/post_img/PAM-RIGID-COMP/rigid_body_sp_test_001.JPEG" data-canonical-src="/post_img/PAM-RIGID-COMP/rigid_body_sp_test_001.JPEG" />

### 模型3
* 将两个part分别放到各自刚体中去，计算重心，将一定的初速度分别*加载至重心点上去*。
* 地板固支四条edge边。
* 设置其中一个part与地板接触。

<img src="/post_img/PAM-RIGID-COMP/2-rigid_body_sp_test_001.JPEG" data-canonical-src="/post_img/PAM-RIGID-COMP/2-rigid_body_sp_test_001.JPEG" />

## 仿真的结果分析
* 将两个part放到同一个刚体中去，计算时会将两个独立的part默认成为一个刚体，在结果中可以看见碰到地板后整体出现旋转，说明两个part变成一个刚体的结果。
* 将两个part分别放到各自刚体中去，计算结果与预期一致，一个碰到地板后反弹，另一个继续下降。

## 讨论
 > 为什么与地板碰撞后出现旋转？
* 可能的原因
** 网格不对称？
** 地板太软有分量？
