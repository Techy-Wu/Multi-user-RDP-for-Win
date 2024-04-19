import os
import logging
import binascii
from win10toast import ToastNotifier

sys_file_path = "C:\\Windows\\System32\\termsrv.dll"
source_file_path = ".\\auto modi\\old\\termsrv.dll"
output_file_path = ".\\auto modi\\modified\\termsrv.dll"
log_path = ".\\auto-modi-log.ini"

find_str = '39813C0600000F84'
sub_str = 'B80001000089813806000090'

toaster = ToastNotifier()

logging.basicConfig(filename = log_path, format='%(asctime)s.%(msecs)03d [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s', datefmt='## %Y-%m-%d %H:%M:%S')
logging.getLogger().setLevel(logging.DEBUG)

logger = logging.getLogger()
logger.info("Program start")

try:
    os.makedirs(".\\auto modi")
    os.makedirs(".\\auto modi\\old")
    os.makedirs(".\\auto modi\\modified")
except:
    logger.error("Cannot make directory")
    toaster.show_toast("系统文件自动重写", "自动重写失败：无法创建文件夹", icon_path=None, duration = 5)
    exit()

# copy and read file
try:
    sys_file = open(sys_file_path, 'rb')
except:
    logger.error("Cannot read system file")
    toaster.show_toast("系统文件自动重写", "自动重写失败：无法读取系统文件", icon_path=None, duration = 5)
    exit()
plain_data = sys_file.read()
sys_file.close()

try:
    source_file = open(source_file_path, 'wb')
except:
    logger.error("Cannot open backup file")
    toaster.show_toast("系统文件自动重写", "自动重写失败：无法生成备份文件", icon_path=None, duration = 5)
    exit()
source_file.write(plain_data)
source_file.close()

# hex to bytes
bytes_data = binascii.hexlify(plain_data)

# bytes to str
str_data = str(bytes_data, encoding='utf-8')

# modifiy data
try:
    start_position = str_data.find(find_str)
except:
    logger.error("Cannot find target string")
    toaster.show_toast("系统文件自动重写", "自动重写失败：找不到指定数据", icon_path=None, duration = 5)
    exit()
output_data_1 = str_data[0:start_position]
output_data_2 = sub_str
output_data_3 = str_data[start_position + len(output_data_2):]
output_data = output_data_1 + output_data_2 + output_data_3

# str to bytes
bytes_out = bytes(output_data, encoding='utf-8')

# bytes to hex
hex_out = binascii.unhexlify(bytes_out) # bytes type

# write to file
try:
    output_file = open(output_file_path, 'wb')
except:
    logger.error("Cannot open midified file")
    toaster.show_toast("系统文件自动重写", "自动重写失败：无法生成新系统文件", icon_path=None, duration = 5)
    exit()
output_file.write(hex_out)
output_file.close()

logger.info("Program completed")
toaster.show_toast("系统文件自动重写", "系统文件已自动重写，待覆盖", icon_path=None, duration = 5)