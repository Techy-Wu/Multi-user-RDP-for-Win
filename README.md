# Multi-user-RDP-for-Win

A small Python script program for detecting the multi-user status, and a related auto-modifying tool attached

检测远程桌面多用户状态的 Python 脚本程序，附有一个对应的系统文件自动修改工具

## Basement 基础

Through modifying the file C:/Windows/system32/termsrv.dll could enable the multi-user function of rdp on Windows 11 (Familiar with Windows Server)

通过修改 C:/Windows/system32/termsrv.dll 可以启用 windows 11 的远程桌面多用户功能（类似 Windows Server）

Ref: [Win11 多用户同时登录远程桌面配置方法](https://www.wyr.me/post/701)

### Detect Method 检测原理

Calculate the md5 value of the system file, backupped source file, and backupped modified file and do a comparison to figure out the status

计算并比较系统文件、备份原文件和备份修改文件的 md5 值，得到当前系统状态

### Modify Method 修改原理

Open the file in HEX mode and substitute the data "39 81 3C 06 00 00 0F 84 XX XX XX XX" with "B8 00 01 00 00 89 81 38 06 00 00 90"

用16进制模式打开文件，搜索 "39 81 3C 06 00 00 0F 84 XX XX XX XX" 替换为 "B8 00 01 00 00 89 81 38 06 00 00 90"

Overwrite the file and restart rdp service

覆写源文件并重启 rdp 服务

## Usage 使用方法

Run "./check.py" to check the status

运行"./check.py"检测当前系统状态

If the status is "need to overwrite", copy the file in folder "./modified" to "C:/Windows/system32" and overwrite the original one

如果提示“需要覆写”，复制"./modified"文件夹里的文件到“C:/Windows/system32”并覆盖原文件

If the status is "need to rewrite", run "./modify.py" then copy the file in folder "./auto modi/modified" to "C:/Windows/system32" and overwrite the original one

如果提示“需要重写”，运行"./modify.py"，然后复制"./auto modi/modified"文件夹里的文件到“C:/Windows/system32”并覆盖原文件

## Reminder 注意事项

This program cannot guarantee the compatibility of the modified file with your system

本程序无法保证修改的文件能适配你当前的系统

As a special reminder, make sure you know how to restore the backupped file to the system folder while Windows cannot start before overwriting the system file

特别提醒，在覆盖系统文件前请一定确保你知道如何在Windows系统无法正常启动时将已备份的系统文件还原到系统目录

