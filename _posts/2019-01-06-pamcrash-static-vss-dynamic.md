---
layout: post
title: " PAMCRASH 静态计算与动态计算 "
tagline: " PAMCRASH Notebook  "
categories: PAMCRASH
author: "Hu Tianyun"
meta: "Springfield"
---
**仅供参考交流，对计算结果的精确性不负任何责任**

# PAMCRASH 静态计算与动态计算的比较

## TIP
pamcrash 一般都是用来算动态问题，如冲击、碰撞等，现有的许多例程也基本都是从显示动态计算开始的；如果使用静态计算有什么不一样的地方。

## 静态
### control 语句
 * ICTRL->Analysis_Type-> static linear 或者其他。

 * ANALYSIS使用的是 ANALYSIS IMPLICIT ,求解器都是用的CRASH。

 * 在静态计算中，时间RUNEND貌似没有什么意义，计算过程中没有体现时间步，自然当THP画图时也不会有时间历程。

 * 静态计算使用IMPLICIT，还需要设置 ECTRL中的一些参数。

 * 静态计算的结果以 *.erfh5 保存。




