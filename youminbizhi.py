# coding:utf-8
import urllib2,re,os
from bs4 import BeautifulSoup

#当前列表页的连接全都存起来
list_arr = []
#讲所有的图片前置连接拿取下来
context_arr = []
def html_read(url):
	html = urllib2.urlopen(url)
	if html.getcode() != 200:
		return
	return html.read()

def html_soup(url):
	html = urllib2.urlopen(url)
	if html.getcode() != 200:
		return
	soup = BeautifulSoup(html.read(),"html.parser",from_encoding="utf-8")
	return soup

def makeDir():
	path = os.getcwd()
	new_path = os.path.join(path,"bizhi")
	if not os.path.isdir(new_path):
		os.mkdir(new_path)

		
if __name__ == "__main__":
	makeDir()
	url = "http://www.gamersky.com/ent/wp/"

	index_soup = html_soup(url)

	aas = index_soup.find_all("a",href=re.compile(r"com/ent/\d+\/\d+\.shtml"))

	for aa in aas:
		list_arr.append(aa['href'])
	for arr in list_arr:
		list_soup = html_soup(arr)
		list_aas = list_soup.find_all("a",href=re.compile(r"com/showimage/id_gamersky"))
		for bb in list_aas:
			imgs = "http://"+bb['href'][59:]
			context_arr.append(imgs)
		
	#根据拿取到的当前页面的所有连接进行再次爬取
	for cc in context_arr:
		link = cc
		print link
		cont = html_read(cc)
		try:
			with open(u'bizhi'+'/'+link[-18:],'wb') as code:
				code.write(cont)
		except Exception, e:
			with open(u'bizhi'+'/'+link[-7:],'wb') as code:
				code.write(cont)
		