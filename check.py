import os
import hashlib
from win10toast import ToastNotifier

def file(path, algorithm):
    size = os.path.getsize(path)  # 获取文件大小，单位是字节（byte）
    with open(path, 'rb') as f:  # 以二进制模式读取文件
        while size >= 1024 * 1024:  # 当文件大于1MB时将文件分块读取
            algorithm.update(f.read(1024 * 1024))
            size -= 1024 * 1024
        algorithm.update(f.read())
    return algorithm.hexdigest()  # 输出计算结果

old_path = ".\\old\\termsrv.dll"
old_md5 = file(old_path, hashlib.md5())

modified_path = ".\\modified\\termsrv.dll"
modified_md5 = file(modified_path, hashlib.md5())

inuse_path = "C:\\Windows\\System32\\termsrv.dll"
inuse_md5 = file(inuse_path, hashlib.md5())

toaster = ToastNotifier()

if inuse_md5 == modified_md5:
    print("Multi user mode is ON")
    toaster.show_toast("多任务远程服务器检测", "多任务状态正常", icon_path=None, duration = 5)
elif inuse_md5 == old_md5:
    print("Multi user mode is OFF, need to OVERRIDE system dll")
    toaster.show_toast("多任务远程服务器检测", "多任务状态异常，需要覆盖系统文件", icon_path=None, duration = 5)
else:
    print("Multi user mode is OFF, need to REWRITE system dll")
    toaster.show_toast("多任务远程服务器检测", "多任务状态异常，需要重写系统文件", icon_path=None, duration = 5)