---
layout: post
title: " ABAQUS 模拟杆中水的运动 "
tagline: " ABAQUS Notebook  "
categories: ABAQUS
author: "Hu Tianyun"
meta: "Springfield"
---
**仅供参考交流，对计算结果的精确性不负任何责任**

# ABAQUS 模拟杆中水的运动  简要的步骤介绍和笔记

![half water imapct](/post_img/half-water-imapct/half-water-imapct.gif  "half water imapct")

## step1 Create the eulerian part   
 * use the bigger eulerian part to cover the water inside.
 
<img src="/post_img/half-water-imapct/f4.png" data-canonical-src="/post_img/half-water-imapct/f4.png" />

## step2 Define the material 
 * define the material of eulerian part

### DO NOT give half-water material
 * Don't worry about the warning about without material when submitting
 
<img src="/post_img/half-water-imapct/f4.png" data-canonical-src="/post_img/half-water-imapct/f1.png" />

## step3 Create the discrete Field
 * Choose the bigger eulerian part the then the half-water to define the discrete Field

<img src="/post_img/half-water-imapct/f4.png" data-canonical-src="/post_img/half-water-imapct/f2.png" />

## step4 Define the general contact
 * Just define it, without the detail property

<img src="/post_img/half-water-imapct/f4.png" data-canonical-src="/post_img/half-water-imapct/f5.png" />

## step5 Define the Load
 * Define the predefined field and choose the discrete field created.

<img src="/post_img/half-water-imapct/f4.png" data-canonical-src="/post_img/half-water-imapct/f3.png" />

*******************************************************
### Result discussion and future improve 
 * Compare the result with the bar without water inside, we can see the bar's movement direction changes backward and forward due to the inertia of water movement.
 * The stress wave propagation is also quite different.
