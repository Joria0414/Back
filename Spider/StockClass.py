#设置类，但看起来好像没太大用
class Spider:
	stockListWebSite= ""
	stockList = []         #添加股票code
	def setCodes(self,codeList):
		self.stockList = codeList





class Stock:
	stockCode=0
	stockName= ""
	date=""
	openValue= ""
	closeValue= ""
	highestValue= ""
	lowestValue= ""
	volumn=""
	def set_stock(self,stock_code,stock_name,date,open_value,close_value,highest_value,lowest_value,volumn):
		self.date = date
		self.closeValue = close_value
		self.openValue = open_value
		self.stockName = stock_name
		self.stockCode = stock_code
		self.highestValue = highest_value
		self.lowestValue = lowest_value
		self.volumn = volumn