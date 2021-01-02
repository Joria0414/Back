from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import datetime #日期时间
import os.path  #路径管理
import sys  #查找脚本名称
from pprint import pprint

import pandas #panda读取数据
#Import the backtrader platform
import backtrader as bt
import matplotlib.pyplot as plt

from MyStrategy import *

plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False   #这两行需要手动设置
_STRATS = {}
_PARAMS = {}
with open(os.getcwd() + "/MyStrategy/datas/StrategyList.csv", 'r', encoding='gbk') as f:
    text = f.readlines()
    for line in text:
        line = line.strip().split(',')
        _STRATS.update({line[0]:getattr(sys.modules[__name__], line[1], 'notfound')})
        ps = {}
        for part in line[2:]:
            p=0
            part = part.split("=")
            if part[1][:5] =="range":
                Range = part[1][6:-1].split(" ")
                p = {part[0]:range(int(Range[0]),int(Range[1]))}
                ps.update(p)
            if part[1][0] =="[":
                D = part[1][1:-1].split(" ")
                D = [int(p) for p in D]
                p = {part[0]:D}
                ps.update(p)
        _PARAMS.update({line[0]:ps})


#构建策略
class TestStrategy(bt.Strategy):
    params =(
        ('exitbars',5),
        ('maperiod1',15),
        ('maperiod2',5),
        ('printlog',True),
    )


    def log(self, txt, dt=None,doprint=False):
        #日志
        if self.params.printlog or doprint:
            dt = dt or self.datas[0].datetime.date(0)
            print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        self.buysellLog = []
        self.dataclose = self.datas[0].close

        self.order = None
        self.buyprice = None
        self.buycomm = None

        #加入移动平均指标
        self.sma1 = bt.indicators.MovingAverageSimple(
            self.datas[0],period=self.params.maperiod1
        )
        # bt.indicators.
        self.sma2 = bt.indicators.MovingAverageSimple(
            self.datas[0],period=self.params.maperiod2
        )
        #self.sma2.plotinfo.plot=False
        # self.sig = self.sma1<self.sma2
        self.sig = btind.CrossOver(self.sma2, self.sma1)


        # 指标
        #bt.indicators.ExponentialMovingAverage(self.datas[0], period=25)
        #bt.indicators.WeightedMovingAverage(self.datas[0], period=25,
        #                                    subplot=True)
        #bt.indicators.StochasticSlow(self.datas[0])
        #bt.indicators.MACDHisto(self.datas[0])
        #rsi = bt.indicators.RSI(self.datas[0])
        #bt.indicators.SmoothedMovingAverage(rsi, period=10)
        #bt.indicators.ATR(self.datas[0], plot=False)

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            #买卖订单已提交或接收
            return

        # 检测是否有订单完成
        # 注意：没有现金时可拒绝
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('BUY EXECUTED,Size: %d,Price: %.2f,Cost: %.2f,Comm: %.2f' %
                         (order.executed.size,
                          order.executed.price,
                          order.executed.value,
                          order.executed.comm))
                self.buysellLog.append('BUY EXECUTED,Size: %d,Price: %.2f,Cost: %.2f,Comm: %.2f\n' %
                         (order.executed.size,
                          order.executed.price,
                          order.executed.value,
                          order.executed.comm))

                self.buyprice = order.executed.price
                # print(self.position)
                self.buycomm = order.executed.comm
            elif order.issell():
                self.log('SELL EXECUTED,Size: %d,Price: %.2f,Cost: %.2f,Comm: %.2f' %
                         (order.executed.size,
                          order.executed.price,
                          order.executed.value,
                          order.executed.comm))
                # print(self.position)
                self.buysellLog.append('SELL EXECUTED,Size: %d,Price: %.2f,Earn: %.2f,Comm: %.2f\n' %
                                       (order.executed.size,
                                        order.executed.price,
                                        order.executed.price*order.executed.size,
                                        order.executed.comm))
            self.bar_executed = len(self)

        #订单取消、拒绝
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        # Write down: no pending order
        self.order = None


    def notify_trade(self,trade):
        # print(trade.ref)
        if not trade.isclosed:
            return

        self.log('OPERATION PROFIT, GROSS %.2f, NET %.2f' %
                 (trade.pnl, trade.pnlcomm))
        self.buysellLog.append('OPERATION PROFIT, GROSS %.2f, NET %.2f\n' %
                 (trade.pnl, trade.pnlcomm))

    def next(self):
        #self.log('Close, %.2f' % self.dataclose[0])

        # 存在订单时，无法提交第二份
        if self.order:
            return

        # 检查是否在市场中
        if not self.position:

            # Not yet ... we MIGHT BUY if ...
            if self.sig>0:

                # BUY, BUY, BUY!!! (with all possible default parameters)
                self.log('BUY CREATE, %.2f' % self.dataclose[0])
                self.buysellLog.append('BUY CREATE, %.2f\n' % self.dataclose[0])
                # Keep track of the created order to avoid a 2nd order
                self.sizer.p.stake = 20
                self.order = self.buy()
        else:

            # 已经在市场中，我们可以卖，此处为买入后超过5个交易日
            if self.sig<0:

                # SELL, SELL, SELL!!! (with all possible default parameters)
                self.log('SELL CREATE, %.2f' % self.dataclose[0])
                self.buysellLog.append('SELL CREATE, %.2f\n' % self.dataclose[0])

                # Keep track of the created order to avoid a 2nd order
                self.order = self.sell()
    def stop(self):
        self.log('(MA Period1 %2d,MA Period2 %2d) Ending Value %.2f' %
                 (self.params.maperiod1,self.params.maperiod2, self.broker.getvalue()), doprint=False)
        self.buysellLog.append('(MA Period1 %2d,MA Period2 %2d) Ending Value %.2f\n' %
                 (self.params.maperiod1, self.params.maperiod2, self.broker.getvalue()))


if __name__ == '__main__':
    # 构建回测架构实体
    cerebro = bt.Cerebro()

    #添加策略
    # Strategy = "双均线策略"
    # p = {"key":Strategy,"maperiod1":range(10,15)}
    cerebro.optstrategy(TestStrategy,maperiod1=[15,16])
    # cerebro.addstrategy(TestStrategy,maperiod1=15)
    # cerebro.addstrategy(TestStrategy,maperiod1=20)
    #数据
    # modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    # datapath = os.path.join(modpath,'datas/orcl-1995-2014.txt')

    #创建数据反馈
    # data = bt.feeds.YahooFinanceCSVData(
    #     dataname=datapath,
    #     # 开始日期
    #     fromdate=datetime.datetime(2013, 1, 2),
    #     # 终止日期
    #     todate=datetime.datetime(2013, 2, 28),
    #     reverse=False)
    data = MyCSVData(
        dataname="MyStrategy/datas/datachoice.csv",
    )

    # 添加数据反馈到回测实体

    cerebro.adddata(data)
    #cerebro.replaydata(data,timeframe=bt.TimeFrame.Weeks,)
    # cerebro.resampledata(data, timeframe=bt.TimeFrame.Weeks, )
    # 设置初始资金
    cerebro.broker.setcash(10000000.0)

    #根据股本加入资金
    cerebro.addsizer(SizerOne)

    #设置手续费
    cerebro.broker.setcommission(commission=0.01)

    # cerebro.addanalyzer(bt.analyzers.Returns,_name = 'returns')

    #回测运行
    results=cerebro.run(optreturn=False)
    # cerebro.plot(style = 'bar')
    # print(results)
    # print(results[0][0].buysellLog)
    # print(p)

    # k = p[0][0].analyzers.returns.get_analysis()
    #绘制结果

    # resultList = []
    # for i,result in enumerate(results):
    #     resultList.append([result[0].analyzers.returns.get_analysis()['rtot'],result[0]])
    # code="600000"
    # fig = cerebro.plotone(strat=resultList[-1][1],style='bar')
    # fig[0].suptitle(Strategy + code)
    # plt.show()
