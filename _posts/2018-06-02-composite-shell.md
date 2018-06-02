---
layout: post
title: " ABAQUS 复合材料层合板壳单元拉伸 "
tagline: " ABAQUS Notebook  "
categories: ABAQUS
author: "Hu Tianyun"
meta: "Springfield"
---
**仅供参考交流，对计算结果的精确性不负任何责任**

# ABAQUS 层合板壳单元拉伸

![composite shell](/post_img/composite-shell/shell-tensile.gif"composite shell")

## step1 正常的3D实体拉伸
 * (有的也可以采用shell，没有厚度)

## step2  网格划分
### 连续壳单元，扫掠划分
如果选用 结构网络,3D stress 则会报错，不能计算
 > Error in job com-1: 1050 elements have missing property definitions. The elements have been identified in element set ErrElemMissingSection.

### 分割实体
 * 如果想要更精细划分并在不同部位选择不同材料，则需要分割实体．

## step3  材料定义
### 弹性模量定义
 * 选用__lamina__，定义__Hashin__破坏准则，损伤演化．

<img src="/post_img/composite-shell/lamina.png" data-canonical-src="/post_img/composite-shell/lamina.png" />

<img src="/post_img/composite-shell/material.png" data-canonical-src="/post_img/composite-shell/material.png" />

### 定义层合板坐标轴
<img src="/post_img/composite-shell/sys.png" data-canonical-src="/post_img/composite-shell/sys.png" />

### 定义层合板，选择坐标轴，输入角度

##  step4 分析步，输出定义
 * 采用了显示动态分析步，时间0.001s
 * 增加输出步长，输出失效变量

<img src="/post_img/composite-shell/step-mesh.png" data-canonical-src="/post_img/composite-shell/step-mesh.png" />

##  step5 载荷定义
 * 位移加载
 * smooth step

<img src="/post_img/composite-shell/load.png" data-canonical-src="/post_img/composite-shell/load.png" />
