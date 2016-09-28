#coding:utf-8
from bs4 import BeautifulSoup
import multiprocessing
import urllib2,os,re

#开始封装函数
#创建文件夹
def dirs():
	 path = os.getcwd()
	 new_path = os.path.join(path,ARCHER)
	 if not os.path.isdir(new_path):
	 	os.mkdir(new_path)

#判断当前页数，并且把当前页的内容传给爬虫
def de_page(page = 1):
	if page == 1:
		return "http://2016ky.com/tupianqu/"+ARCHER+"/"
	else:
		return "http://2016ky.com/tupianqu/"+ARCHER+"/index_" + str(page) + ".html"

#根据url获取网页的soup DOM 实例化
def get_html_soup(url):
	if not url:
		return 0
	html = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8')
	return soup
#根据url获取网页的read信息
def get_html_read(url):
	if not url:
		return 1
	try:
		html = urllib2.urlopen(url).read()
	except Exception, e:
		print "chuwentile!!!!url:" + url
		get_html_read(url)
	
	return html

def save_file(down,content):
	# down = down.strip('/')
	# print down.strip("/")
	try:
		with open(ARCHER + "/" + down[-10:],'wb') as code:
			code.write(content)
	except Exception, e:
		try:
			with open(ARCHER + "/" + down[-8:], 'wb') as code:
				code.write(content)
		except Exception, e:
			return

#根据网址获取当前页面下所有列表下面的图片  83
def de_paqu(page = 1):
	arr = []
	#拿取当前页码下的网址
	url1 = de_page(page)

	#根据网址拿取到页面内容,并且实例化DOM树
	soup = get_html_soup(url1)
	links = soup.find_all('a',href=re.compile(r"tupianqu/"+ARCHER+"+/1"))
	for link in links:
		arr.append(url + link['href']) 
	for ar in arr:
		sooo = get_html_soup(ar)
		imgs = sooo.find_all('img',src=re.compile(r"cache"))
		for img in imgs:
			img_src = img['src']
			print str(page) + " : " + str(img_src)
			#再次根据图片的url拿取图片的2进制内容
			content = get_html_read(img_src)
			if content == 1:
				continue
			else:
			    save_file(img_src,content)

	PAGE+=1
	de_paqu(PAGE)

#当前网址的区域
ARCHER = 'katong'
#当前网址的主网址
url = "http://2016ky.com"
global PAGE 
PAGE = 1

if __name__ == "__main__":
	# url1 = "http://2016ky.com/tupianqu/"+ARCHER+"/"

	#创建文件夹
	dirs()
	print "mk ok!"
	#开始爬取
	# de_paqu(1)
	#使用多线程来爬去
	print "go!"
	p = multiprocessing.Process(target=de_paqu,args=(PAGE,))
	PAGE +=1
	p1 = multiprocessing.Process(target=de_paqu,args=(PAGE,))
	PAGE +=1
	p2 = multiprocessing.Process(target=de_paqu,args=(PAGE,))
	PAGE +=1
	p3= multiprocessing.Process(target=de_paqu,args=(PAGE,))
	p.start()
	p1.start()
	p2.start()
	p3.start()
