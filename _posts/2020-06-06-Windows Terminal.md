---
layout: post
title: "Windows Terminal"
description: "Win10优化设置"
categories: [windows]
tags: [learn, note]
author: wukong
redirect_from:

  + /2020/01/01/

---

# Windows Terminal

## 启动路径配置

在 Microsoft Store 安装 Windows Terminal、ubantu
打开配置文件，将用不到的环境设置 "hidden: true", 增加新的环境。

``` json
  {
    "guid": "{7882cb27-2b3b-4512-86ce-40b8bc6aff9c}",
    "hidden": false,
    "name": "unen.xyz",
    "commandline": "ssh root@47.112.162.128",
    "icon": "C:\\icon\\ali.png"
}

```

## powershell配置文件

powershell配置文件 [参考](https://forsenergy.com/zh-cn/windowspowershellhelp/html/9c82251c-6f0d-416a-9c3c-77838218531b.htm)

``` shell
# 显示路径
$profile
# 判断是否存在配置文件 若不存在手动创建
test-path $profile
```

### python wokon

启动python虚拟环境 [参考](http://hk.uwenku.com/question/p-dnkemkwb-ew.html)

workon是批處理腳本。如果你從PowerShell運行它，它會在一個新的CMD子進程中啓動，在那裏做它的事情，然後退出並返回到PowerShell提示符。由於子進程無法修改其父進程，所以當您返回到PowerShell時，將丟失workon.bat所做的所有修改。

写入Microsoft. PowerShell_profile.ps1

``` powershell
function workon($environment) {
    & cmd /k workon.bat $environment
}
```

## 免密登录ssh

服务器、主机分别生成公钥、私钥对 `ssh-keygen`
将主机的公钥 `id_rsa.pub` 发送到服务器，
在服务器 `.ssh/` 文件夹下执行

``` powershell
    touch authorized_keys
    chmod 600 authorized_keys
    cat id_rsa.pub >> authorized_keys
```

测试是否实现免密登录 `ssh root@xx.xxx.xxx.xxx`

## 树莓派

开启frp参考[教程](https://www.jianshu.com/p/00c79df1aaf0 )
启动命令 `./frpc -c ./frpc.ini`
宝塔[教程](https://www.bilibili.com/video/BV1kE411C7hz)
开启宝塔 `sudo ./bt_run` 关闭宝塔 `./bt_prog kill`
开启samba[教程](https://tlanyan.me/setup-samba-in-raspberry-pi/)
挂载U盘[教程](https://zhuanlan.zhihu.com/p/35061575)
有线替换Wifi `取消路由器中PI ip和MAC的绑定、路由器禁用PI wifi、重启路由器有线连接PI、手动绑定ip和MAC`
关闭灯、wifi[link](https://zhuanlan.zhihu.com/p/138038622)
