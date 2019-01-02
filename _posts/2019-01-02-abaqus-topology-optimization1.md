---
layout: post
title: " ABAQUS 拓扑优化例子 1 "
tagline: " ABAQUS Notebook  "
categories: ABAQUS
author: "Hu Tianyun"
meta: "Springfield"
---
**仅供参考交流，对计算结果的精确性不负任何责任**

# ABAQUS 拓扑优化 例程-1

## 结果
例程来源于【youtube abaqusman】

![opt-1](/post_img/abaqus-topology-opt-1/res.png  "opt-1")

*********************************************


## 模型建立 model.png

<img src="/post_img/abaqus-topology-opt-1/model.png"  data-canonical-src="/post_img/abaqus-topology-opt-1/model.png" />

## 优化步骤
### 优化job建立

<img src="/post_img/abaqus-topology-opt-1/opt_1.png"  data-canonical-src="/post_img/abaqus-topology-opt-1/opt_1.png" />

### 选择优化函数
选择应变能和体积分数作为优化函数。
<img src="/post_img/abaqus-topology-opt-1/opt_2.png"  data-canonical-src="/post_img/abaqus-topology-opt-1/opt_2.png" />

### 优化函数的限制

<img src="/post_img/abaqus-topology-opt-1/opt_3.png"  data-canonical-src="/post_img/abaqus-topology-opt-1/opt_3.png" />

## 结果
### 没有优化的结果
<img src="/post_img/abaqus-topology-opt-1/res-no-opt.png"  data-canonical-src="/post_img/abaqus-topology-opt-1/res-no-opt.png" />

