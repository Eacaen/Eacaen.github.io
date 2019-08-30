---
layout: post
title: " PAMCRASH 集中质量点冲击平板 "
tagline: "PAMCRASH Notebook"
categories: PAMCRASH
author: "Hu Tianyun"
meta: "Springfield"
---
**结果仅供交流，对计算结果的精确性不负任何责任**

> 结果.gif-等待加载

<img src="/post_img/PAM_MASS_IMPACT/node_mass3-part-cont_001.gif" data-canonical-src="/post_img/PAM_MASS_IMPACT/node_mass3-part-cont_001.gif" />

## 模型介绍
* 一块壳单元平板，四边固支，一个node位于某一壳单元中部以上3MM处，一块单独由壳单元构成的part与节点以OTMCO(RBE3)的形式相连接；一个集中质量附加在node上面。
* 材料卡103，输入材料参数，定义塑性曲线。
* 给与part1和node一个向下的初速度。
* 采用了node-to-surface接触，选定part1和node为从面，part2为主面，接触厚度**0.5MM**。

<img src="/post_img/PAM_MASS_IMPACT/mass_impact_model.png" data-canonical-src="/post_img/PAM_MASS_IMPACT/mass_impact_model.png" />

## 仿真的预期结果和实际结果
* 按照理论上的想法，集中点质量应该与平板产生node-to-surface接触，在冲击下产生**点状**冲击破坏。
* 实际的结果可以看出，集中点质量node并没有与平板产生接触而是直接穿过，当壳单元与平板距离达到接触厚度后，开始计算接触，平板产生破坏。
* 整个过程能量变化正确。
<img src="/post_img/PAM_MASS_IMPACT/mass_impact_result.png" data-canonical-src="/post_img/PAM_MASS_IMPACT/mass_impact_result.png" />

## 讨论
 > 为什么没有产生预期的效果？
 * 估计在PAMCRASH中，接触的计算只是在part之间，而一个单独的质量点无法归于一个part，所以即使在接触中选择了该node，也无法进行接触计算。
