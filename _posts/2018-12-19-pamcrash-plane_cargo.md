---
layout: post
title: " PAMCARSH 机身框坠撞刚性地面"
tagline: " PAMCARSH Notebook  "
categories: PAMCARSH
author: "Hu Tianyun"
meta: "Springfield"
---
**仅供参考交流，对计算结果的精确性不负任何责任**

> 结果

<img  src="/post_img/plane_cargo/demo3_1-remesh_001.gif"  data-canonical-src="/post_img/plane_cargo/demo3_1-remesh_001.gif" />

## 模型介绍
网格模型来源于Hypermesh教程demo3-1.hm中的飞机典型结构。
 * 为了节约计算时间，重新划分网格，网格大小改为50mm，保持原来结构中共节点状态；
 * 长桁、肋板与蒙皮使用铆钉（PLINK）连接；
 * 增加一个集中质量点，使用One to mutiple constraint 将节点与壁板结构连接；
 * 地面使用刚性壳单元，约束重心的6个自由度；
 * 给定整体Z向的速度和重力加速度；
 * 接触：结构与地面的主从接触；自接触；边对边接触；长桁与蒙皮接触。
 * 
### 单位：Ton，mm，s
### 导出单位及数量级
 * 力：N
 * 应力：MPa
 * 密度：9.9e-9
 * 杨氏模量：28000

### 网格数量
|网格类型|数量|
|2D Element|2602|
|Plink|144|

<img  src="/post_img/plane_cargo/ps.png" width = "300" data-canonical-src="/post_img/plane_cargo/ps.png" />

## 材料卡片
### SHELL 材料卡片
 * 103模型，自定义塑性曲线
<img  src="/post_img/plane_cargo/mat.png" width = "300" data-canonical-src="/post_img/plane_cargo/mat.png" />

### PLink 材料
 * 224材料与302材料的区别；
 * 某些参数必须定义，否则报错无法计算；
 * 使用link manager 检查连接是否成功；
 * 对比提交计算即可看出区别；
<img  src="/post_img/plane_cargo/plink.png" width = "300" data-canonical-src="/post_img/plane_cargo/plink.png" />
<img  src="/post_img/plane_cargo/plink2.png" data-canonical-src="/post_img/plane_cargo/plink2.png" />

## 结果

### 能量
经过短暂重力加速，动能有所上升而后下降；整体的能量变化守恒。
<img  src="/post_img/plane_cargo/energy.png" width = "300" data-canonical-src="/post_img/plane_cargo/energy.png" />