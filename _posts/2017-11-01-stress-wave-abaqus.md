---
layout: post
title: " ABAQUS 模拟霍普金森杆应力波 "
tagline: " ABAQUS Notebook  "
categories: ABAQUS
author: "Hu Tianyun"
meta: "Springfield"
---
**仅供参考交流，对计算结果的精确性不负任何责任**

# ABAQUS 模拟应力波传播

材料常数：

![Impact](/post_img/ABAQUS-BAR/CodeCogsEqn.gif  "Impact")

杆尺寸：

	入射杆长度10，直径10；透射杆长度100，直径10；


## 结果
![Impact simulation](/post_img/ABAQUS-BAR/imapct.gif  "Impact simulation")

*********************************************

做个小笔记，记下分析步骤。

## Assembly
### 两杆对心，距离 5 。
![Assembly](/post_img/ABAQUS-BAR/assembly.png  "Assembly")



## Step
### 定义分析步step1，**显示动力学分析**，修改时间。
![StepcontactDefine](/post_img/ABAQUS-BAR/StepcontactDefine.png  "StepcontactDefine")



### FieldoutputSet 提高输出帧数。
![FieldoutputSet](/post_img/ABAQUS-BAR/FieldoutputSet.png  "FieldoutputSet")




### historyOutput，设置历史输出
 *  输出目标为透射杆的应力 S33 和 速度 V3，方便结果绘图。可添加多个杆进行输出。
 *  【注】历史变量输出太多计算中会报错，可减少输出或修改可输出最大值。
![historyOutput](/post_img/ABAQUS-BAR/historyOutput.png  "historyOutput")




## Interaction
### 定义接触参数，属性默认。
![contactPropertyDef](/post_img/ABAQUS-BAR/contactPropertyDef.png  "contactPropertyDef")



### 选择接触面，定义接触面属性。
![contactSurface](/post_img/ABAQUS-BAR/contactSurface.png  "contactSurface")



## Load
### 定义边界条件，锁定位移和旋转，杆件只有轴向位移。
![boundaryConditionSet](/post_img/ABAQUS-BAR/boundaryConditionSet.png  "boundaryConditionSet")



### 定义入射杆速度场。
 *  【注】速度场选择整个杆子的 set ，不是选择一个面。
![predefineField](/post_img/ABAQUS-BAR/predefineField.png  "predefineField")



## 结果讨论 
### 在 T=0.05 时开始碰撞，产生一个压缩波。
![timeImpact](/post_img/ABAQUS-BAR/timeImpact.png  "timeImpact")



### 压缩波反射形成拉伸波。
![TensileWave](/post_img/ABAQUS-BAR/TensileWave.png  "TensileWave")



### 杆上速度和应力变化。
![Wave](/post_img/ABAQUS-BAR/Wave.png  "Wave")
![Vectory](/post_img/ABAQUS-BAR/Vectory.png  "Vectory")


