# coding:utf-8
# 这个作为潜伏在阴影中的客户端
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)	#初始化自身
s.connect(('127.0.0.1',8000))
print("我对面的可是传说中的 最强服务端？\\n 等待您的指令")
while True:
	data = s.recv(512).decode('utf-8')
	print(data)