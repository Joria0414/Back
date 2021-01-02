#编写网络获取的处理函数
import requests
import os


def getHTMLText(url):           #解析html成text
	try:
		r = requests.get(url)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""

def download(code,start,end,path=u"./"):
	if path[-1] != '/':     #规范路径
		path += '/'
	codetype = '0'          #codetype 是该网站接口设置，调整出现板块。对于000001,codetype == 0,为 上证指数， codetype == 1，为平安银行
	if code[0]=='0':
		codetype = '1'
	os.system('wget -c \"http://quotes.money.163.com/service/chddata.html?code='+codetype+code+'&start='
	          +start+'&end='+end+'&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP\" -O '
	          +path+code+'.csv')    #调用os进行下载



