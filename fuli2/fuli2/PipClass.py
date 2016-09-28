#coding:utf-8
import os

class PipC:
    def __init__(self):
        print ('PipC_OK!')
    def down_beautifulSoup(self):
        try:
            from bs4 import BeautifulSoup
        except:
            os.system("sudo pip2 install beautifulsoup4")

    def down_xiancheng(self):
        try:
            import multiprocessing
        except:
            os.system("sudo pip2 install multiprocessing")
