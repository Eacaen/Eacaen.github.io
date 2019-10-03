---
layout: post
title: " PAMCRASH-ABAQUS 吸能结构压缩结果对比 "
tagline: "PAMCRASH Notebook"
categories: PAMCRASH
author: "Hu Tianyun"
meta: "Springfield"
---
**可以看到两个不同的软件在设置上的不同造成结果的巨大差异。【结果仅供交流，对计算结果的精确性不负任何责任】**


## 模型介绍
### 不同的吸能管结构介绍
 * 管的外形具有不同的曲率，边缘处也可以进行适当的处理
 * 目的都是尽可能的让更多的材料参与压缩变形，产生塑性形变从而可以吸收更多的能量。

### 软件设置
 * 材料相同。
 * 边界设置上
 	- 两端的刚体设置不同
 	- 材料接触参数设置应该如何取值才能得到相同的边界
 * 相同的网格密度，pam会穿透，原因。？

## 详细内容
<img src="/post_img/PAM-ABAQ-COMPRESS/page1.png" data-canonical-src="/post_img/PAM-ABAQ-COMPRESS/page1.png" />

<img src="/post_img/PAM-ABAQ-COMPRESS/page2.png" data-canonical-src="/post_img/PAM-ABAQ-COMPRESS/page2.png" />

<img src="/post_img/PAM-ABAQ-COMPRESS/page3.png" data-canonical-src="/post_img/PAM-ABAQ-COMPRESS/page3.png" />