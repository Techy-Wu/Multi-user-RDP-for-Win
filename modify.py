import sys
import os

HexTable = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

fin  = open('.\\old\\termsrv.dll', 'r')
fout = open('.\\out.bin', 'wb')

for i in range(0, 65536, 1):
	fout.write('\x00'.encode())

for aLineData in fin:
	DataLen  = HexTable[aLineData[1]]*16 + HexTable[aLineData[2]]
	DataAddr = HexTable[aLineData[3]]*16*16*16 + HexTable[aLineData[4]]*16*16 + \
	           HexTable[aLineData[5]]*16 + HexTable[aLineData[6]]
	DataType = HexTable[aLineData[7]]*16 + HexTable[aLineData[8]]

	# Data Offset
	fout.seek(DataAddr)
	for i in range(0, DataLen*2, 2):
		DataContent = HexTable[aLineData[9+i]]*16 + HexTable[aLineData[10+i]]
		StrContent = chr(DataContent)
		fout.write(StrContent)

	print(hex(DataLen),hex(DataAddr),hex(DataType))

fin.close()
fout.close()