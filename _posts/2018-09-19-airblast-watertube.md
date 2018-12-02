---
layout: post
title: " ABAQUS 水管受爆炸冲击 "
tagline: " ABAQUS Notebook  "
categories: ABAQUS
author: "Hu Tianyun"
meta: "Springfield"
---
**仅供参考交流，对计算结果的精确性不负任何责任**

# ABAQUS 模拟杆水管受到爆炸冲击
【结果】水管受冲击后，水从开口出射出，水管压扁，基座部分破坏；因为水管存在和水的射出，带走了部分能力，能过减弱基座受到了的应力。
![Airblast](/post_img/Airblast/res.gif  "Airblastl")

## step1 材料定义，装配
 * 水管装配时全部没入欧拉体中，基座底部固支，水管与基座fixed

<img src="/post_img/Airblast/material.png" data-canonical-src="/post_img/Airblast/material.png" />


## step2  接触定义
### 直接定义全体的通用接触（具体作用有待考察）
### 水管的自接触
* 水管材料使用的橡胶，在受airblast时受压上下内表面可能会接触

<img  src="/post_img/Airblast/self-contact.png" width = "300" heigth = "300" data-canonical-src="/post_img/Airblast/self-contact.png" />

### 定义Airblast
* abaqus 中使用TNT 来定义，指定爆炸点和接触面

<img  src="/post_img/Airblast/air-blast.png" width = "400" heigth = "400" data-canonical-src="/post_img/Airblast/air-blast.png" />

## step3 离散出水，划分网格
### 划分DisField 
<img  src="/post_img/Airblast/water-dis.png" width = "400" heigth = "400" data-canonical-src="/post_img/Airblast/water-dis.png" />

### mesh 
>Total number of nodes: 98289

>Total number of elements: 86618

     6618 linear hexahedral elements of type C3D8R
     
     80000 linear hexahedral elements of type EC3D8R
