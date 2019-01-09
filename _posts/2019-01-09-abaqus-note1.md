---
layout: post
title: " ABAQUS Notebook-1"
tagline: " ABAQUS Notebook  "
categories: ABAQUS
author: "Hu Tianyun"
meta: "Springfield"
---

## note
### abaqus 壳单元
输出壳单元厚度，看到厚度方向的变化

### 接触不收敛，穿透太大
 * 细化接触区域网格
 * normal Behavior 中“硬”接触改为软接触--指数
 * 接触不稳定
   * 接触面突然释放，单一节点不稳定接触或者突然反转导致发散。
   *  Abaqus/Standard 中在 Edit step 中选择 自动稳定
   *  仅对接触对使用接触阻尼，避免应用到全部节点上去。
 * 检查接触阻尼的影响

### 显示动力学分析 ABAQUS/Explicit
 > blog.sina.com.cn/s/blog_87dd1ae70101956n.html
 * 最初为了模拟高速冲击问题，在这类问题的求解中*惯性*发挥了主导性作用。当求解动力平衡的状态时，非平衡力以应力波的形式在相邻的单元之间传播。由于最小稳定时间增量一般地是非常小的值，所以大多少问题需要大量的时间增量步。
 * 也可以用于准静态过程（guasi-static process）