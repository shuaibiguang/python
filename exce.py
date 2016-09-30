#coding:utf-8
import xlrd,urllib2,re,os
from bs4 import BeautifulSoup

data = xlrd.open_workbook('8888888888888888888888888.xls')

table = data.sheets()[0]
nrows = table.nrows


def down(url,dir,type):
	if type != 2:
		url = "http://res.baopintao.com/"+url
	img = urllib2.urlopen(url);
	name = url.split("/")
	# print img
	sum = len(name) -1
	name = name[sum]



	lujing = os.getcwd()
	lujing = lujing.split("\\")
	sums = len(lujing) -1
	lujing = lujing[sums]

	if lujing != dir:
		os.chdir(dir)		


	with open(name,'wb') as code:
		code.write(img.read())

def chuliduo(cont,dir):
	soup = BeautifulSoup(cont,"html.parser",from_encoding="utf-8")
	aas = soup.find_all("img")
	for aa in aas:
		down(aa["src"],dir,2)


def is_dir(dir):
	path = os.getcwd()
	new_path = os.path.join(path,dir)
	if not os.path.isdir(new_path):
		os.mkdir(new_path)

def huilai():
	os.chdir("../")

for i in range(nrows ):
	if i !=0:
		lielit = table.row_values(i)
		tu1 = lielit[1]
		tu2 = lielit[2]
		content = lielit[3]
		dirName = str(long(lielit[5]))

		is_dir(dirName)
		chuliduo(content,dirName)

		print long(lielit[5])

		down(tu1,dirName,1)
		down(tu2,dirName,1)

		huilai()
		# break