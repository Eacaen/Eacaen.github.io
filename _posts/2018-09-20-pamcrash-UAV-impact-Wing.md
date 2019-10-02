---
layout: post
title: " PAMCRASH 无人机撞击机翼 "
tagline: "PAMCRASH Notebook"
categories: PAMCRASH
author: "Hu Tianyun"
meta: "Springfield"
---
**结果仅供交流，对计算结果的精确性不负任何责任**

> 结果[.gif 等待加载。。。]

<img src="/post_img/UAV-WING/r1.gif" data-canonical-src="/post_img/UAV-WING/r1.gif" />

<img src="/post_img/UAV-WING/r2.gif" data-canonical-src="/post_img/UAV-WING/r2.gif" />

## 项目介绍
### 问题来源
* 航拍无人机使用广泛，但是事故越来越多，影响正常航班，带来巨大安全隐患。通过无人机模型冲击机翼仿真分析，观察在不同的速度和角度下对机翼结构造成的影响；与适航条例中的鸟撞飞机相关条款对比，说明无人机碰撞与鸟撞的异同之处，提出对机翼结构的改进；为以后适航条例修改提供数值依据。

### 工况介绍
* 以市场占有率很高的大疆精灵系列无人机为案例，测量绘制3D模型，添加材料后得到其有限元模型。
* 无人机主要结构重量集中于4个电机，相机云台和电池之中，这些部件在碰撞过程中重量大，惯性大，会对机翼结构造成较大的破坏。
* 通过改变无人机与机翼碰撞区域的接触角度和相对的飞行速度，可以获得不同工况下的结果，进而对比各个工况下的不同严重程度的破坏。

<img src="/post_img/UAV-WING/uav.png" data-canonical-src="/post_img/UAV-WING/uav.png" />

## 能量分析
* 在整个过程中能量守恒。

<img src="/post_img/UAV-WING/energy.png" data-canonical-src="/post_img/UAV-WING/energy.png" />