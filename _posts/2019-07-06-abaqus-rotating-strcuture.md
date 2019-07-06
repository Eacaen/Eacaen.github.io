---
layout: post
title: " ABAQUS 旋转叶片 "
tagline: " ABAQUS Notebook  "
categories: ABAQUS
author: "Hu Tianyun"
meta: "Springfield"
---
**仅供参考交流，对计算结果的精确性不负任何责任**

# ABAQUS 旋转叶片

例程来源于【youtube abaqusman】
## 结果【gif】

<img src="/post_img/ABAQUS-rotating-blade/blade1.gif"  data-canonical-src="/post_img/ABAQUS-rotating-blade/blade1.gif" />

<img src="/post_img/ABAQUS-rotating-blade/blade2.gif"  data-canonical-src="/post_img/ABAQUS-rotating-blade/blade2.gif" />

*********************************************


## 模型建立 
### 模型
 * 原计划是想把叶片看作刚体，在参考点上给与相应的约束和角速度（在pam-crsah中可以直接完成，显示计算），但是在abaqus中这样做却没有效果。
 * 使用两种模型和不同的求解器进行尝试。

### 步骤
#### 将模型耦合到参考点上去

<img src="/post_img/ABAQUS-rotating-blade/blade1-1.PNG"  data-canonical-src="/post_img/ABAQUS-rotating-blade/blade1-1.PNG" />

<img src="/post_img/ABAQUS-rotating-blade/blade2-1.PNG"  data-canonical-src="/post_img/ABAQUS-rotating-blade/blade2-1.PNG" />

#### 加载
 * 约束参考点的BC条件
 
 * 给*整个模型*加载角速度
 
<img src="/post_img/ABAQUS-rotating-blade/blade1-1.PNG"  data-canonical-src="/post_img/ABAQUS-rotating-blade/blade1-1.PNG" />


### 求解器
 * 一般模型肯定是使用的显式动力学求解，但是变成刚体模型后，直接提交abaqus不能求解，报错无法确定时间步长。
 *  改用隐式动力学求解可以求解。
 *  改用显式动力学，*【定义时间步长】*求解可以求解。