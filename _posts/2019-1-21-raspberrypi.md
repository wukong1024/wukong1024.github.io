---
layout: post
title: "Raspberry Raspberry PIPI"
description: "Raspberry PI"
categories: [hardware]
tags: [learn, Raspberry PI, system]
author: wukong
redirect_from:
  - /2019/1/21/
---

# Raspberry PI

[TOC]

## 准备工作

### 硬件

+ 树莓派Raspberry3b+主板
+ 外接显示屏，支持HDMI接口（系统默认只支持HDMI显示）
+ 3.5寸触摸屏显示器-LCD屏幕（需要系统单独按照驱动）
+ 16GB TF卡
+ 读卡器
+ 鼠标（usb有线）
+ 键盘（usb有线）
+ HDMI连接线
+ 5V2A的电源和micro usb线

### 软件

+ SD Formatter（格式化工具）
+ Win32DiskImager（烧录工具）
+ 2018-11-13-raspbian-stretch.img（）镜像文件

### 配置

用"SD Formatter"格式化TF卡后，再将镜像烧录到其中 插入树莓派 接入显示器，鼠标，键盘后启动。

**重点**：烧录完成后，不要点击格式化TF卡！！！

## 无线连接

<img src="https://wu-kong.oss-cn-beijing.aliyuncs.com/img/20190201101022.png" alt="" width=50% height=50% align=left>

<img src="https://wu-kong.oss-cn-beijing.aliyuncs.com/img/20190201101201.png" alt="" width=50% height=50% align=right>

### putty

在TF-卡中新建文件 ssh （系统默认不开机ssh）

登录路由器管理界面查询树莓派的ip地址

<img src="https://wu-kong.oss-cn-beijing.aliyuncs.com/img/20190122084934.png" alt="" width=50% height=50% align=center>

服务器下载并安装putty 输入上图中的IP 开始连接默认用户名 pi  密码  respberry

<img src="https://wu-kong.oss-cn-beijing.aliyuncs.com/img/20190122090321.png" alt="" width=50% height=50% align=center>

### VNC Viewer

putty登录后在终端输入 `sudo raspi-config`

选择 5.INterfacing Options

再选择 P3 VNC

服务器下载并安装VNC Viewer

<img src="https://wu-kong.oss-cn-beijing.aliyuncs.com/img/20190122090900.png" alt="" width=50% height=50% align=center>

### IP与MAC地址绑定

登录路由器管理界面后，在高级设置中

<img src="https://wu-kong.oss-cn-beijing.aliyuncs.com/img/20190122105919.png" alt="" width=50% height=50% align=center>

添加IP与MAC地址绑定

更改VNC分辨率`vncserver -geometry 1200x1366`

更改后用IP+端口号登陆

## 学习笔记

### Linux教程

#### 关机重启

`ctrl + alt + t`打开终端

``` plaintext
#关机
sudo shutdown -h now
sudo poweroff
shutdown -r重启  -c 取消 now 现在  20:25 今天的20:25  +10 10分钟后关机

#重启
sudo reboot
sudo shutdown -r now

#注销
logout :退出 注销

```

#### 系统目录说明

/ 根路径

这是Linux系统的“根”目录，也是所有目录结构的最底层。在UNIX以及和它兼容的系统中，”/“是一个单独的目录。

/boot

这个目录下包含系统启动文件（boot loader），例如Grub，Lilo或者Kernel，以及initrd，system.map等配置文件。

/sys

这个目录下包含内核、固件以及系统相关文件。

/sbin

包含系统操作和运作所必需的二进制文件以及管理工具，主要就是可执行文件。类似WINDOWS下的EXE文件。

/bin

包含单用户模式下的二进制文件以及工具程序，比如cat，ls，cp这些命令。

/lib

包含/sbin和/bin目录下二进制文件运行所需要的库文件。

/dev

内含必需的系统文件和驱动器。

/etc

内含系统配置文件，其下的目录，比如 /etc/hosts, /etc/resolv.conf, nsswitch.conf, 以及系统缺省设置，网络配置文件等等。以及一些系统和应用程序的配置文件。

/**home**

每一个用户的在这个目录下，都会单独有一个以其**用户名**命令的目录，在这里保存着用户的个人设置文件，尤其是以 profile结尾的文件。但是也有例外，root用户的数据就不在这个目录中，而是单独在根路径下，保存在单独的/root文件夹下。

/**media**

一个给所有可移动设备比如光驱、USB外接盘、软盘提供的常规挂载点。路径显示为`/media/用户名/U盘名`

/mnt

临时文件系统挂载点。比如，你并不想长期挂载某个驱动器，而是只是临时挂载一会U盘烤个MP3之类的，那么应该挂载在这个位置下。

/opt

在Linux系统中，这个目录用到的并不多，opt是 可选系统程序包（Optional Software Packages）的简称。这个目录在UNIX系统，如Sun Solaris用途要广泛的多。

/usr

用户数据目录，包含了属于用户的实用程序和应用程序。这里有很多重要的，但并非关键的文件系统挂载这个路径下面。在这里，你会重新找到一个 bin、sbin 和 lib目录，其中包含非关键用户和系统二进制文件以及相关的库和共享目录，以及一些库文件。

/usr/sbin

包含系统中非必备和并不是特别重要的系统二进制文件以及网络应用工具。

/usr/bin

包含用户的非必备和并不是特别重要的二进制文件。

/usr/lib

保存着/usr/sbin以及/usr/bin中二进制文件所需要的库文件。

/usr/share

“平台无关”的共享数据目录。

/usr/local

是/usr下的二级目录，这里主要保存着包含系统二进制文件以及运行库在内的本地系统数据。

/var

这个路径下通常保存着包括系统日志、打印机后台文件（spool files）、定时任务（crontab）、邮件、运行进程、进程锁文件等。这个目录尤其需要注意进行日常的检查和维护，因为这个目录下文件的大小可能会增长很快，以致于很快占满硬盘，然后导致系统便会出现各种奇奇怪怪的问题。

/tmp

顾名思义，这是一个临时文件夹，专门用来保存临时文件，每次系统重启之后，这个目录下的”临时”文件便会被清空。同样，/var/tmp 也同样保存着临时文件。两者唯一的不同是，后者 /var/tmp目录保存的文件会受到系统保护，系统重启之后这个目录下的文件也不会被清空。

/proc

这个目录是驻留在系统内存中的虚拟（psuedo，伪）文件系统，其中保存的都是文本格式的系统内核和进程信息。

> LINUX系统目录结构图

<img src="https://wu-kong.oss-cn-beijing.aliyuncs.com/img/20190122122449.png" alt="" width=50% height=50% align=center>

#### 基本命令

| 命令                 | 全称                    | 解释                    |
| -------------------- | :---------------------- | :---------------------- |
| man + 命令           | Manual                  | 手册 查询其他命令用法   |
| pwd                  | Print working directory | 打印当前工作目录        |
| cd                   | Change directory        | 切换目录                |
| ls + -l              | List files              | 列出目录下的文件        |
| mkdir                | Make directory          | 建立文件夹              |
| rmdir                | Remove directory        | 删除文件夹              |
| cat                  | Concatenate             | 串联？查看文件 合并文件 | s |
| touch                | touch                   | 新建文件                |
| rm                   | remove                  | 删除指定文件            |
| clear                | clear                   | 清屏                    |
| tree                 | tree                    | 文件树                  |
| cp                   | cope                    | 复制                    |
| mv                   | move                    | 移动/重命名             |
| grep+字符串+文件名   | grep                    | 搜索                    |
| echo + 字符串 > 文件 | > 新建 >>增加           | 输出内容到文件          |

``` shellscript

rm扩展: -r 删除目录文件   -f强制删除无提示

tree扩展:  -d 只显示目录

cp/mv扩展: -r 复制目录文件 -i 提示覆盖

cat扩展:   -b空行不编号  -n全部编号

cat + 文件[文件>新文件] 合并文件

grep扩展:  -n显示行号   -v反向选择   -i忽略大小写  ^a  ke$


tar -cvf py.tar 01.py 02.py 03.py  文件打包(不压缩)

tar -xvf py.tar [-C dictionary]  文件解包  -z压缩为.gz   -j压缩为.bz2

sudo apt install|remove|upgrade  软件名  sl 小火车 htop 系统进程

chown: Change owner 改变所有者

chgrp: Change group 改变用户组

chmod: Change mode 改变模式
insmod：Install module 安装模块
rmmod：Remove module 删除模块
lsmod：List module 列表模块

sudo是superuser do的简写

查看linux版本号：uname -a

比较两个文件：diff 1.c 2.c 或cmp 1.c 2.c

设置文件的读写权限：chmod u+w 1.c(增加文件拥有者对1.c写的权限)
chmod g-r 1.c( 删除工作组对1.c读的权限)
chmod o+x 1.c(增加其他用户对1.c的执行权限)
chmod a-w 1.c(删除所有用户对1.c写的权限)
chmod 777 -R aaa  更改目录及子文件子目录全部权限
chmod u=rwx,g=rw,o=r aa.py

u 所有者 g 所属组 o 其他用户
r=4 w=2 x=1

查看运行的进程：ps process status
杀掉某个线程：kill 1186（1186是线程号）

date  查询当前系统时间

df -h   disk free 显示磁盘剩余空间     -h 人性化的方式显示文件大小

alias ll="ls -lh"  自定义命令的别名
unalias ll 取消别名

which ls 查看命令位置
```

### 树莓派实验室

#### RPi.GPIO 模块使用基础

``` python
#导入模块
import RPi.GPIO as GPIO
#针脚编号
GPIO.setmode(GPIO.BCM)
#忽略警告s
GPIO.setwarnings(False)
#配置通道
GPIO.setup(channel,GPIO.IN,pull_up_down=GPIO.PUD_UP)
#输入 读取GPIO针脚的值
GPIO.input(channel)
#输出 设置GPIO针脚的输出状态 1/GPIO.HIGH/True
GPIO.output(channel,state)
#边缘检测 RISING FALLING BOTH
GPIO.wait_for_edge(channel, GPIO.RISING)

#清理
GPIO.cleanup()
#检测Raspberry Pi主板的修订版本
GPIO.RPI_REVISION
#检测RPI.GPIO的版本
GPIO.VERSION

#线程回调 边缘检测
def my_callback(channel):
    print('这是一个边缘事件回调函数！')
    print('在通道 %s 上进行边缘检测'%channel)
    print('该程序与您的主程序运行在不同的进程中')
#回调加入开关防抖
GPIO.add_event_detect(channel, GPIO.RISING, callback=my_callback,bouncetime=200)
#停止边缘检测事件
GPIO.remove_event_detect(channel)

```

##### 使用 RPi.GPIO 模块的输入（Input）功能

```python
"""
1.polling轮询 循环定时检查输入值
2.interruots中断   边缘检测  检测临界值 falling edge rising edge
"""

```

#### 18B20温度传感器

坏了  2.68又买了一个 等快递
`https://www.jianshu.com/p/1aeed4cfd431`

#### DHT11温湿度传感器

参考[项目](https://github.com/yfgeek/rpi-TempRuntime)

##### 1.DHT11温湿度传感器的安装

电阻：4.7--10KΩ

<div align=center>

<hr>
<img src="https://wu-kong.oss-cn-beijing.aliyuncs.com/img/5.png" alt="" width=50% height=50% align=center>
接线原理图
<hr>

<img src="https://wu-kong.oss-cn-beijing.aliyuncs.com/img/CB270D99CBC55EDECA8609F091E31B56.png" alt="" width=50% height=50% align=center>
接线实物图
</div>

##### 2.收集传感器的信息

安装依赖的库

```python
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo python setup.py install
sudo pip install RPi.GPIO
```

下载项目

```python
sudo mkdir /env
cd env
git clone https://github.com/yfgeek/rpi-TempRuntime.git
```

修改项目

```shell
cd /env/rpi-TempRuntime
sudo nano DHT11-WITHOUT-LCD.py
```

修改`humidity, temperature = Adafruit_DHT.read_retry(sensor, 26)`中的26改为自己的GPIO#序号，`humidity, temperature = Adafruit_DHT.read_retry(sensor, 4)`，保存退出。

历史数据以JSON格式存储在/env/rpi-TempRuntime/web/data/min（或者hour）

##### 3.caddy部署

基本配置[教程](https://pimylifeup.com/raspberry-pi-caddy-web-server/)

```shell
curl https://getcaddy.com | bash -s personal
sudo mkdir /etc/caddy
sudo nano /etc/caddy/Caddyfile
```

输入

``` plaintext
:80 localhost:8080 {
    /env/rpi-TempRuntime/web
    gzip
}
```

<div align=center>
<hr>
<img src="https://wu-kong.oss-cn-beijing.aliyuncs.com/img/20190213095626.png" alt="" width=50% height=50% align=left>
2019-02-12 DHT11温湿度监视图
<hr>
</div>