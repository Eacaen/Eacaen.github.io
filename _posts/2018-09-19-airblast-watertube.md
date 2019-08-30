---
layout: post
title: " ABAQUS 水管受爆炸冲击 "
tagline: " ABAQUS Notebook  "
categories: ABAQUS
author: "Hu Tianyun"
meta: "Springfield"
---
**仅供参考交流，对计算结果的精确性不负任何责任**

# ABAQUS 模拟杆水管受到爆炸冲击
【结果】水管受冲击后，水从开口出射出，水管压扁，基座部分破坏；因为水管存在和水的射出，带走了部分能力，能过减弱基座受到了的应力。
![Airblast](/post_img/Airblast/res.gif  "Airblastl")

## step1 材料定义，装配
 * 水管装配时全部没入欧拉体中，基座底部固支，水管与基座fixed

<img src="/post_img/Airblast/material.png" data-canonical-src="/post_img/Airblast/material.png" />


## step2  接触定义
### 直接定义全体的通用接触（具体作用有待考察）
### 水管的自接触
* 水管材料使用的橡胶，在受airblast时受压上下内表面可能会接触

<img  src="/post_img/Airblast/self-contact.png" width = "300" heigth = "300" data-canonical-src="/post_img/Airblast/self-contact.png" />

### 定义Airblast
* abaqus 中使用TNT 来定义，指定爆炸点和接触面

<img  src="/post_img/Airblast/air-blast.png" width = "400" heigth = "400" data-canonical-src="/post_img/Airblast/air-blast.png" />

## step3 离散出水，划分网格
### 划分DisField 
<img  src="/post_img/Airblast/water-dis.png" width = "400" heigth = "400" data-canonical-src="/post_img/Airblast/water-dis.png" />

### mesh 
>Total number of nodes: 98289
>Total number of elements: 86618
    6618 linear hexahedral elements of type C3D8R 
    80000 linear hexahedral elements of type EC3D8R

***
## 2019-08-30 更新
***
### 关于air blast 的 CONWEP 模型
 * 参阅abaqus帮助文档
  >  In Abaqus/Explicit the CONWEP model can be used for air blast loading on solid and structural elements, without the need to model the fluid medium。

<img  src="/post_img/Airblast/conwep.PNG"   data-canonical-src="/post_img/Airblast/conwep.PNG" />

在有入射波载荷的ABAQUS中，可以使用几种不同的建模方法，需要不同的方法来应用入射波载荷。对于仅涉及固体和结构元件的问题（例如，入射波场是由空气中的波引起的），波荷载的施加大致类似于分布的表面荷载。这可能适用于对车辆或建筑物上空气中爆炸荷载的分析（参见图34.4.6-6所示的“示例：结构上的气流荷载”）。在ABAQUS/Explicit中，Conwep模型可用于固体和结构元件上的空气爆炸荷载，无需对流体介质进行建模。ABAQUS示例问题指南第9.1.9节“Conwep爆炸荷载下夹层板的变形”是爆炸荷载问题的一个例子。

入射波荷载（conwep荷载除外）也可应用于梁结构；这是一种常用的船舶振打分析建模方法，也适用于承受爆炸荷载的钢框架建筑。入射波荷载可应用于二维或三维梁单元上定义的表面。然而，入射波荷载只能应用于三维梁的瞬态动力分析，其中梁的流体惯性是确定的。不能在框架单元、线弹簧单元、三维开放截面梁单元或三维欧拉-伯努利梁上定义入射波荷载。

在水下爆炸分析中（如图34.4.6-4和图34.4.6-5所示，承受水下爆炸荷载的船舶或水下车辆），也使用有限元模型对流体进行离散，以捕捉流体刚度和惯性的影响。对于这些涉及固体和声学元件的问题，存在两种声压场公式。首先，利用声学元件模拟介质中的总压力，包括入射场的影响和整个系统的响应。或者，声学元件只能用来模拟介质对波荷载的响应，而不能模拟波脉冲本身。前一种情况称为“全波”公式，后一种情况称为“散射波”公式。
入射波相互作用也被用来模拟冲击结构或声场的声场。结构散射的声场或通过结构传播的声音可能会引起兴趣。通常情况下，声散射和传播问题都是用稳态动力学程序的散射公式来模拟的。瞬态程序也可以用类似于水下爆炸分析问题的方式使用。

### 散射波和全波公式

只有在施加入射波荷载时，总波公式和散射波公式之间的区别才是相关的。总波公式比散射波公式更接近于结构荷载：声介质的边界被指定为加载面，并在其上施加时变荷载，从而在声介质中产生响应。该响应等于介质中的总声压级。散射波公式利用了这样一个事实：当声介质为线性时，介质中的响应可以分解为入射波和散射场之和。当声学介质因可能的流体空化而非线性时，必须使用全波公式（见《ABAQUS理论指南》第6.3.1节“因入射膨胀波场而产生的荷载”）。

#### 散射波公式

当流体力学可以描述为线性时，观察到的总声压可分解为两部分：已知的入射波和由入射波与结构和/或流体边界相互作用产生的“散射”波。当这种叠加适用时，通常直接求“散射”波场解。当使用散射波公式时，声节点处的压力仅定义为总压力的散射部分。在这种情况下，应加载声学结构界面处的声学和固体表面。

#### 全波公式

当声学介质能够产生空化，使流体力学行为非线性时，全波公式（见《ABAQUS理论指南》第2.9.1节“耦合声学结构介质分析”）尤其适用。如果问题包含规定压力历史的弯曲或有限范围边界，则也应使用该方法。在这种情况下，只有外部声表面应加载入射波，入射波源必须位于流体模型外部。任何可能存在于该外部声学边界上的阻抗或不反射条件仅适用于不包括规定入射波场的声学解部分（即，只有散射场受不反射条件影响）。因此，所施加的入射波载荷将进入问题域，而不受外表面非反射条件的影响。  

在全波公式中，声压自由度代表总动态声压，包括入射波和散射波的贡献，以及在abaqus/explicit中，流体空化的动态效应。压力自由度不包括可指定为初始条件的声静压（见“ABAQUS/标准和ABAQUS/明确的初始条件”第34.2.1节中的“定义初始声静压”）。该声静压仅用于确定声元节点的空化状态，不会对其公共湿界面处的声学或结构网格施加任何静载荷。它不适用于使用ABAQUS/标准的分析。
