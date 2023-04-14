#!/usr/bin/python
import sys
import socket

def Wake(port=8):
	mac="".join(sys.argv[2].split(':'))
	mac="".join(sys.argv[2].split('-'))
	data = b"\xFF\xFF\xFF\xFF\xFF\xFF" + bytes().fromhex(mac) * 16
	s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
	try:
		s.sendto(data,(sys.argv[1],port))
		print('[+] 已发送唤醒请求！')
	except:
		print('[!] 发送失败，请检查IP地址或域名！')
	s.close()

if len(sys.argv)<2:
	print('Usage: Python3',sys.argv[0],'[IP Address] [MAC Address] [UDP Port,default=8]')
	print('Example: Python3',sys.argv[0],'192.168.1.3 28-6E-D4-89-37-BA')
	print('         Python3',sys.argv[0],'192.168.1.3 28-6E-D4-89-37-BA 9')
elif len(sys.argv)<4:
	Wake()
else:
	Wake(int(sys.argv[3]))
