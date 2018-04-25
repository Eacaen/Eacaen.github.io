---
layout: post
title: " ABAQUS 运动相机防水壳密封页片 "
tagline: " ABAQUS Notebook  "
categories: ABAQUS
author: "Hu Tianyun"
meta: "Springfield"
---
**仅供参考交流，对计算结果的精确性不负任何责任**

# ABAQUS　运动相机防水壳密封页片

淘宝上买了运动相机防水壳，用过的都知道运动相机防水壳采用是确实一种十分暴力的方法，借助页片变形的力直接将密封圈固定在壳体上，但是这样的方法完全依赖页片变形，我在淘宝上先后购买了两款不同页片形状的壳子，第一款壳子的页片已连续损坏两次，都是由于在开闭壳子时圆形边角开裂而造成应力集中，而购买的第二款新壳子就直接去掉了原有的边角，并将密封圈在密封时嵌入壳体．就这个改进我感到还是满意的，改进原因也十分简单．借机复习一下ＡＢＡＱＵＳ使用，看看到底改进了多少．

![two-cc](/post_img/ABAQUS-WPBlade/crack.jpg  "two")
## 简化模型和材料参数
原始曲面模型比较复杂，塑料材料也不好确定，但是我只是要看到大概的趋势，所以对模型进行了简化，材料也只给定了弹性模量和泊松比．

![simple-model](/post_img/ABAQUS-WPBlade/simple-model1.png "simple-model1")

## 简化受力和边界条件
固定限制页片底部Ｙ方向和边界处Ｘ方向的位移，给定页片爪子处强制的位移．

![simple-model](/post_img/ABAQUS-WPBlade/simple-model2.png "simple-model2")

## 结果分析

### [款式一] 完整页片
在完整的款式一页片处，应力集中于圆孔两侧，最大位移位于爪子处．

![wholes1](/post_img/ABAQUS-WPBlade/0/wholes1.png "wholes1")
![wholeu1](/post_img/ABAQUS-WPBlade/0/wholeu1.png "wholeu1")

### [款式一] 裂纹页片
#### 裂纹

裂纹直接画图产生，没有使用ＡＢＡＱＵＳ裂纹功能．（不会）
![hole](/post_img/ABAQUS-WPBlade/1/hole.png "hole")

#### 结果
在款式一发生裂纹的页片处，应力集中于圆孔裂纹对面，应力值稍有下降，整体位移感觉没有巨大改变．

![holes](/post_img/ABAQUS-WPBlade/1/holes.png "holes")
![holeu](/post_img/ABAQUS-WPBlade/1/holeu.png "holeu")

### [款式二] 去角页片
在款式二页片，直接将圆口去掉，消除了孔边应力集中，整体位移感觉没有什么改变．

![wholes2](/post_img/ABAQUS-WPBlade/2/wholes2.png"wholes2")
![wholeu2](/post_img/ABAQUS-WPBlade/2/wholeu2.png "wholeu2")

## 结论分析
对比以上三个结果，看到款式一设计上个人还是感觉存在一些不足，尤其是在页片塑料选材和制造上如果不行的话，由于应力集中和拆装时容易侧重一边，确实容易像我一样多次掰断页片．

第二款页片，在节省了材料的同时，消除了应力集中．整体的位移没有什么变化，应该不会影响密封性能．（关于最终载荷和位移对密封的影响分析是否正确还有待考察）．

## ＥＮＤ
款式二刚到货，防水性能还有待测试．但是就目前来看，款式二的改进确实比款式一好多了．


