---
layout: post
title: " Spring in PAMCRASH & ABAQUS"
tagline: " PAMCRASH Notebook  "
categories: PAMCRASH
author: "Hu Tianyun"
meta: "Springfield"
---
**仅供参考交流，对计算结果的精确性不负任何责任**

> 结果

<img  src="/post_img/pam-aba-spring/aba_res1.gif"  data-canonical-src="/post_img/pam-aba-spring/aba_res1.gif" />
<img  src="/post_img/pam-aba-spring/mass-spring-0.002-0.1_001.gif"  data-canonical-src="/post_img/pam-aba-spring/mass-spring-0.002-0.1_001.gif" />

## spring/dashpot in abaqus and pamcrash

### spring/dashpot in pamcrash
弹簧的定义在pamcr	ash中较abaqus麻烦，主要是在坐标系定义中和材料定义。
 * 坐标（R，S，T）定义方法一：使用4个node确定一个坐标系，弹簧方向是node1和node2方向；方法二：node1和node2和一个frame坐标系。

<img  src="/post_img/pam-aba-spring/pam-spring-cos.PNG" data-canonical-src="/post_img/pam-aba-spring/pam-spring-cos.PNG" />

 * 弹簧材料定义：在pam中与弹簧相关的单元材料种类很多，有beam-spring,6dof-spring等等等，弹簧主要是需要劲度系数k和一个很小的质量（否则不能计算）。
<img  src="/post_img/pam-aba-spring/pam-spring-mat.PNG" width = "300" data-canonical-src="/post_img/pam-aba-spring/pam-spring-mat.PNG" />

### spring/dashpot in abaqus
手册vol4,32-1
 * CAE中可以定义与地面的弹簧和两节点弹簧，同时给定劲度系数k；
 * 没有质量；

## 结果对比
pamcrash中k=50,m=0.1，根据T=2*pi*(m+CM/k)^0.5,在弹簧质量忽略时，周期T=0.28s。

<img  src="/post_img/pam-aba-spring/pam-spring-dis.PNG" width = "300" data-canonical-src="/post_img/pam-aba-spring/pam-spring-dis.PNG" />

### pam 中弹簧质量与质量有不同比例
#### pamcrash中给节点一个初速度。
 * 1：1；
<img  src="/post_img/pam-aba-spring/pam-spring-e2.PNG" width = "300" data-canonical-src="/post_img/pam-aba-spring/pam-spring-e2.PNG" />

 * 1：50；
<img  src="/post_img/pam-aba-spring/pam-spring-e1.PNG" width = "300" data-canonical-src="/post_img/pam-aba-spring/pam-spring-e1.PNG" />

 * 1：1e9；
<img  src="/post_img/pam-aba-spring/pam-spring-e3.PNG" width = "300" data-canonical-src="/post_img/pam-aba-spring/pam-spring-e3.PNG" />

> 有以上三个对比可以发现：理论上当弹簧质量比大于10或15时其质量可忽略，小于时可取系数1/3，但是在pam中，即使达到50时能量也不是很稳定，只在动能/内能达到峰值时短暂相等；当质量相差很大时，总的能量才相等；弹簧有质量时，动能也不好对应上。


### aba 中弹簧质量与质量有不同比例
#### abaqus中给节点一个初速度
abaqus 中没有定义弹簧质量，结果总能守恒

<img  src="/post_img/pam-aba-spring/aba-spring-e2.PNG" width = "300" data-canonical-src="/post_img/pam-aba-spring/aba-spring-e2.PNG" />

#### abaqus中给节点一个初位移
abaqus 中给定初始位移后，释放，内能+动能-外力做功 = con，

<img  src="/post_img/pam-aba-spring/aba-spring-e1.PNG" width = "300" data-canonical-src="/post_img/pam-aba-spring/aba-spring-e1.PNG" />
