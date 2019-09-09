---
layout: post
title: "AidLearning"
description: "可以在安卓上直接使用的linux系统"
categories: [system]
tags: [learn, linux]
author: wukong
redirect_from:
  - /2019/08/28/
---
# AidLearning

参考链接

+ [How to Enable OpenSSH Server in Windows 10](https://winaero.com/blog/enable-openssh-server-windows-10)
+ [AidLearning-FrameWork](https://github.com/aidlearning/AidLearning-FrameWork)

## 安装与配置

下载AidLearning并安装，安装后等待安装后重启动，登录账号(wukong1996@163.com)

## 电脑通过ssh链接

Windows设置>>应用>>应用与功能>>管理可选功能>>添加OpenSSH客户端

进入 'C:\windows\system32\Openssh'，加入系统环境变量，执行ssh-keygen生成密钥文件，默认保存在'C:\Users\Wukong\.ssh'目录下。

通过 '<http://192.168.1.112:8910/upload>'将生成的密钥文件 id_rsa 和 id_rsa.pub 上传到 AidLearning。

打开cmd通过'ssh u0_a311@手机IP -p8022'连接手机。

使用powershell连接：

+ 主机手机ip
+ 端口 8022
+ 方法 公钥
+ 用户名 u0_a311
+ 私钥 C:\Users\Wukong\.ssh\id_rsa
+ 私钥密码 无

通过 '<http://192.168.1.112:8080/files/>' 进行AidLearning的文件资源管理
