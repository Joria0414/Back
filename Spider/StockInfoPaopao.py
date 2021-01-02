from bs4 import BeautifulSoup
import time
from StockClass import *
from SpiderWeb import *

#code是股票代码，start是开始时间，end是结束时间

stockListSite = 'http://www.bestopview.com/stocklist.html'  #获取股票列表的网址


# 根据日期获取股票code列表
def getCodeList():
	htmlText = getHTMLText(stockListSite)      #获取网页
	soup = BeautifulSoup(htmlText,"lxml")       #从这里开始是解析网页，可以自行查看该网页结构
	divLst = soup.find_all(class_='result')
	codeList  =[]                               #code列表
	for i in divLst:
		for j in i.ul:
			if str(j) == "\n":
				continue
			t = str(j).split(">")
			ls = t[2].split("(")
			code = ls[1].split(")")[0]
			codeList.append(code)           #获取到code，并添加入数组
	return codeList


def getCodeData(code, start="19800101", end="today",path='./'):    # 根据时间下载
	if end.__eq__("today") or end.__eq__(""):
		end = time.strftime("%Y%m%d", time.localtime())  # 获取当天时间
	if start.__eq__(""):
		start = "19800101"
	try:
		download(code, start=start, end=end, path=path)
		print("下载成功："+code+" begin:"+start+" end:"+end)
	except Exception as e:
		print(e)
		download(code, start='19800101', end='time.strftime("%Y%m%d", time.localtime())', path=path)
		print("下载不一定成功：" + code + " begin:" + start + " end:" + end+",请进行检查")




def getAllStockInfo(start, end,path='./'):         #date指结束时间
	listSpider = Spider()
	listSpider.stockListWebSite = stockListSite
	codeList = getCodeList()  # 获取股票的codeList
	for code in codeList:   #获取各个个股数据并添加，可以通过子线程
		getCodeData(code, start, end,path)






