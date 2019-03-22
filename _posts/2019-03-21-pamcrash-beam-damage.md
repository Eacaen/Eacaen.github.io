---
layout: post
title: " PAMCRASH 梁单元的破坏测试 "
tagline: "PAMCRASH Notebook"
categories: PAMCRASH
author: "Hu Tianyun"
meta: "Springfield"
---
**结果仅供交流，对计算结果的精确性不负任何责任**

> 结果

<img src="/post_img/PAM_BEAM_DEMO1/beam1_001.gif" data-canonical-src="/post_img/PAM_BEAM_DEMO1/beam1_001.gif" />

## 模型介绍
* 一根线，长度100，beam单元数20。
* 材料卡212，输入材料参数，定义塑性曲线。
* 直接固支两端，中部施加一个集中力。

<img src="/post_img/PAM_BEAM_DEMO1/beam_model.png" data-canonical-src="/post_img/PAM_BEAM_DEMO1/beam_model.png" />


## 结果
* 梁在中部被拉断后，整个节点连接发散，没有单元删除的显示，在卡片的定义中也没有找到单元删除的控制语句。
* 有待查找相关的控制语句

<img src="/post_img/PAM_BEAM_DEMO1/beam_result.png" data-canonical-src="/post_img/PAM_BEAM_DEMO1/beam_result.png" />

