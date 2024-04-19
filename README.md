# Multi-user-RDP-for-Win

A small python script for detecting the multi-user statues

检测远程桌面多用户状态 python 脚本

## Basement 基础

Modifing the file C:/windows/system32/termsrv.dll could enable the multi-user function of rdp on windows 11 (Familiar to Windows Serser)

通过修改 C:/windows/system32/termsrv.dll 可以使能 windows 11 的远程桌面多用户功能（类似 Windows Server）

[Win11 多用户同时登录远程桌面配置方法](https://www.wyr.me/post/701)

## Detect Method

Calculate the md5 value of the system file, backuped source file and backuped modified file and do comparation to figure out the status

计算并比较系统文件、备份原文件和备份修改文件的 md5 值，得到当前系统状态

## Modify Method

Open the file in HEX mode and substitute the data "39 81 3C 06 00 00 0F 84 XX XX XX XX" with "B8 00 01 00 00 89 81 38 06 00 00 90"

用16进制模式打开文件，搜索 "39 81 3C 06 00 00 0F 84 XX XX XX XX" 替换为 "B8 00 01 00 00 89 81 38 06 00 00 90"

Overwriter the file and restart rdp service

覆写源文件并重启 rdp 服务