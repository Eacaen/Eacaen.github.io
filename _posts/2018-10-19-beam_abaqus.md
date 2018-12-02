---
layout: post
title: " ABAQUS 梁单元与实体梁比较"
tagline: " ABAQUS Notebook  "
categories: ABAQUS
author: "Hu Tianyun"
meta: "Springfield"
---
**仅供参考交流，对计算结果的精确性不负任何责任**

> 结果参考
	http://www.020fea.com/a/5/152/11521.html

<img  src="/post_img/ABAQUS-Beam/ques.png"  data-canonical-src="/post_img/ABAQUS-Beam/ques.png" />

## ABAQUS 梁单元与实体梁
【比较结果】梁单元是理想的梁模型，实际上是一根线，需要赋予梁的截面属性和主轴（材料）方向；实体梁就和普通的实体一样绘制。

## ABAQUS 梁单元
### 3D，可变形模型，线
### 材料

<img  src="/post_img/ABAQUS-Beam/beam-sec.png" width = "300" data-canonical-src="/post_img/ABAQUS-Beam/beam-sec.png" />
1

### 对线mesh，显示节点编号

<img  src="/post_img/ABAQUS-Beam/show-nodes.png" width = "300" data-canonical-src="/post_img/ABAQUS-Beam/show-nodes.png" />

### 显示梁模型

<img  src="/post_img/ABAQUS-Beam/show-beam.png" width = "500"  data-canonical-src="/post_img/ABAQUS-Beam/show-beam.png" />

### Load
#### 体现使用梁单元优势 
 * 可以直接输出剪力，弯矩 SF，SM
 * 载荷、约束定义直接在节点上

### 结果
#### 可以看到明显的阶跃间断

<img  src="/post_img/ABAQUS-Beam/SF2-1.png"  data-canonical-src="/post_img/ABAQUS-Beam/SF2-1.png" />

## ABAQUS 实体梁
使用实体梁的困难在于如何添加载荷和约束，在梁单元中，这些都是直接添加在节点上的，在实体单元中如果使用两端的面约束，梁的变形就和理想的不一样；载荷是作用于节点上的，在实体中，建立参考点，然后将：
 * 面耦合到参考点，这样做的话，力均布到面上，其实与实际的截面剪力分布不和；
 * 节点到参考点约束节点耦合；

### mesh
划分网格时注意将面的几个中点找出来，便于选取载荷和约束的位置

### 约束节点耦合
 * 将参考点与面上
<img  src="/post_img/ABAQUS-Beam/node-cop.png" width = "600" data-canonical-src="/post_img/ABAQUS-Beam/node-cop.png" />


### 载荷约束在中点（节点）
<img  src="/post_img/ABAQUS-Beam/load.png"  data-canonical-src="/post_img/ABAQUS-Beam/load.png" />

### 结果
#### 可以切片观察面上的力和弯矩
<img  src="/post_img/ABAQUS-Beam/3d-beam.png" width = "600"  data-canonical-src="/post_img/ABAQUS-Beam/3d-beam.png" />

#### 看不到明显的阶跃间断
 * 由于是实体梁，与理想的梁单元相比，应力联系看不到明显的阶跃间断
<img  src="/post_img/ABAQUS-Beam/3d-beam-res.png" width = "600"  data-canonical-src="/post_img/ABAQUS-Beam/3d-beam-res.png" /> 

## 讨论