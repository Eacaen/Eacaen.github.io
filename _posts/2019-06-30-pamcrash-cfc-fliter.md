---
layout: post
title: " PAMCRASH CFC-滤波器还原 "
tagline: "PAMCRASH Notebook"
categories: PAMCRASH
author: "Hu Tianyun"
meta: "Springfield"
---
**结果仅供交流，对计算结果的精确性不负任何责任**

[知乎](https://zhuanlan.zhihu.com/p/39632483)

[论文](https://web.wpi.edu/Pubs/ETD/Available/etd-050610-115613/unrestricted/Mongiardini_dissertation.pdf)

[CFC Filter Analysis Object (Digital Filters Option)](https://www.weisang.com/en/documentation/cfcfilteranalysis_en/)

[CFCFilter (FPScript)](https://www.weisang.com/en/documentation/cfcfilter_en/)

[CFC Filter Calculation](https://www.weisang.com/en/documentation/cfcalgorithm_en/)

*The difference equation describes a two-pole filter. To achieve a 4-pole filter, the data must pass through the two-pole filter twice: once forward and once backward. This prevents phase shifts.*

【结果】

<img src="/post_img/PAM-CFC-Filter/1-10000.png" data-canonical-src="/post_img/PAM-CFC-Filter/1-10000.png" />

<img src="/post_img/PAM-CFC-Filter/0.2-10000.png" data-canonical-src="/post_img/PAM-CFC-Filter/0.2-10000.png" />


# 尝试还原pam-viewer后处理中CFC滤波
## CFC(Channel Frequency Class)
输出参考节点的加速度值，一般都需要选用一种滤波器进行加速度数据处理，在pam中自带了几种滤波器；为进行加速度滤波，查阅相关资料，SAE J211/1 MAR95 ，FAA等，对于此类加速度，推荐使用CFC-60。

## 使用python还原了一下基本过程

### 单次正向滤波
 * 单次正向滤波存在波形比正常的大且存在相位差引起的时间滞后。
<img src="/post_img/PAM-CFC-Filter/1-10000-1.png" data-canonical-src="/post_img/PAM-CFC-Filter/1-10000-1.png" />

### 两次滤波
 * 正反滤波后波形与正常的CFC-60一致
 * 需要对head 和 tail的异常数据进行处理


## 讨论
### 对于输出的节点数据的处理，与pam中*OCTL的输出频率*有关，相同的滤波器对于不同的采样频率数据的处理效果不同
### 滤波器的相位移动
