---
layout: post
title: "BBB Notebook ５ 串口使用"
tagline: " BBB Notebook ５ "
categories: beagleboard-black
author: "Hu Tianyun"
meta: "Springfield"
---

# beagleboard black 笔记 <５>
使用串口
[使用Beaglebone Black的串口UART](http://blog.csdn.net/wyt2013/article/details/16846027)

# PC 端
## 使用USB 转串口
插入USB 转串口，查看电脑是否有pl2303 驱动，查看电脑串口名字

	lsmod |grep pl2303
	dmesg | tail -f  
	lsmod | grep usbserial
	dmesg | grep ttyUSB0

## 安装串口工具
[Ubuntu安装配置串口通讯工具minicom&&cutecom](http://blog.csdn.net/gatieme/article/details/45310493)

安装minicom完成后

	//回环测试
	sudo minicom -b 9200 -o -D /dev/ttyUSB0 
	sudo minicom -b 9200 -o -D /dev/ttyO0/1/2/4
效果是键盘按下什么键，都会返回重复的【显示两次】。

# BBB开启串口
## 进入目录，查看串口的IO口
	dtc -I dtb -O dts BB-UART1-00A0.dtbo > BB-UART1-00A0.dts
	cat BB-UART1-00A0.dts //看到pin号

## 挂载device tree来启动UART1

	echo BB-UART1 > $SLOTS  

## 改变波特率，发送信息
	
	stty -F /dev/ttyO1  9600
	echo "What a wonderful day" > /dev/ttyO1 
在配置完好的PC端就可以看到消息

## 【注意】改变IO口的属性
一开始我以为，BBB的串口IO口属性是默认的，尝试了好多次都只能使用uart0，其他的都不行，后来想到这和pwm波的一样要配置属性。


	/sys/devices/platform/ocp# config-pin -l P9.24
	default gpio gpio_pu gpio_pd uart can i2c pru_uart pruin

	/sys/devices/platform/ocp# config-pin -l P9.14　//与串口IO口不同
	default gpio gpio_pu gpio_pd pwm

	config-pin P9.24 uart
	config-pin P9.26 uart　

	cat ocp:P9_26_pinmux/state　//查看属性

## UART0
 > 直接把串口转usb模块的TXD，RXD和地线连到对应的引脚上（如图所示），无需进行任何配置，立刻就能开始使用了。
uart0配置完波特率之后可以直接使用。

 ![uart0](/post_img/BBB-img/pinuart0.jpeg  "uart0")