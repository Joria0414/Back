# boll带策略
#
# 突破压力线卖出，跌破支撑线买入
#
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt
import backtrader.indicators as btind

class StrategyThree(bt.Strategy):
    params =(
        ('maperiod',20),
        ('printlog',True),
    )

    def log(self, txt, dt=None,doprint=False):
        #日志
        if self.params.printlog or doprint:
            dt = dt or self.datas[0].datetime.date(0)
            self.buysellLog += '%s, %s' % (dt.isoformat(), txt)
    def __init__(self):
        self.buysellLog = ""
        self.dataclose = self.datas[0].close

        self.order = None
        self.buyprice = 0
        self.buycomm = 0
        self.buytime = 0

        # 使用自带的indicators中自带的函数计算出支撑线和压力线，period设置周期，默认是20
        self.top = btind.BollingerBands(self.datas[0], period=self.params.maperiod).top
        self.bot = btind.BollingerBands(self.datas[0], period=self.params.maperiod,plot=False).bot

        self.Crossovertop = btind.CrossOver(self.dataclose, self.top,plotname='压力线交叉')
        self.Crossoverbot = btind.CrossOver(self.dataclose, self.bot,plotname='支撑线交叉')

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            #买卖订单已提交或接收
            return

        # 检测是否有订单完成
        # 注意：没有现金时可拒绝
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('买入,股份: %d,价格: %.2f,花费: %.2f,手续费用: %.2f\n' %
                         (order.executed.size,
                          order.executed.price,
                          order.executed.value,
                          order.executed.comm))

                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            elif order.issell():
                self.log('卖出,股份: %d,价格: %.2f,获得: %.2f,手续费用: %.2f\n' %
                         (order.executed.size,
                          order.executed.price,
                          order.executed.price * abs(order.executed.size),
                          order.executed.comm))

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('订单 被取消/拒绝\n')

        # Write down: no pending order
        self.order = None

    def notify_trade(self,trade):
        if not trade.isclosed:
            return

        self.log('交易利润, 总利润 %.2f, 纯利润 %.2f\n' %
                 (trade.pnl, trade.pnlcomm))

    def next(self):

        if self.order:
            return
            # 入场
        if self.Crossoverbot < 0 :
            # 买入总资产30%
            self.newstake = self.broker.getvalue()*0.3/ self.dataclose[0]
            self.newstake = int(self.newstake / 100) * 100
            self.sizer.p.stake = self.newstake
            self.buytime+=1
            self.order = self.buy()
            # 出场
        elif self.Crossovertop> 0 and self.buytime > 0:
            self.order = self.sell()
            self.buytime = 0
    def stop(self):
        self.log('(布林带周期 %2d日) 最终总资产 %.2f\n' %
                 (self.params.maperiod, self.broker.getvalue()), doprint=True)