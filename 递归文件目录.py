# coding:utf-8
import os

def pp(path,level = 1):
	aa = os.listdir(path)
	for a in aa:
		qian = ''
		if level != 1: 
			print("| "*(level-1)+"|__ "+a)
		else:
			print(a)
		# 判断a里面是否有目录
		paths= path.replace("\\","\\\\")
		if os.path.isdir(paths+r"\\"+a):
			# 判断是目录
			kevek = level+1
			# print(paths+r'\\'+a)
			pp(paths+r"\\"+a,kevek)
		else:
			print("   Size:"+str(os.path.getsize(paths+r"\\"+a)/1024.0))
	return 1
pp(os.getcwd())
