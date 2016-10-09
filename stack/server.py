# -*- coding: utf-8 -*-
import socket
arr = []
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',8000))
s.listen(5)
print("以我之名 在此召唤，起来吧，服务端!")  #服务端好像乱码了,3版本的没问题，看来上次还是把py搞坏了
while True:
	sock,addr = s.accept()	 #进入监听状态,潜伏在阴影中的客户端，颤抖吧
	# 如果接受到信息打印出来
	print("是你连接进来了?",addr)
	arr.append(sock)
	if len(arr) == 3:
		while True:
			inn = input("开始下达命令:").encode('utf-8')
			for aa in arr:
				aa.send(inn)
	else:
		print ('还有%s个'%(3-len(arr)))
