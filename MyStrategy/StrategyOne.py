# 双均线策略
#
# 猜想：使用10日的移动平均线作为短期均线，60日的移动平均线作为长期均线，
# 当短期均线金叉长期均线的时候，买入总资产10%的股票；当短期均线死叉长期均线的时候，
# 卖出清仓。银行股票市值一般比较大，被操纵的可能性比较小，并且买卖的交
# 易者比较多，信息扩散比较快，市场相对比较有效。
#
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt
import backtrader.indicators as btind

class StrategyOne(bt.Strategy):
    # 参数
    params =(
        ('maperiod1',10),
        ('maperiod2',60),
        ('printlog',True),
    )

    def log(self, txt, dt=None,doprint=False):
        #日志
        if self.params.printlog or doprint:
            dt = dt or self.datas[0].datetime.date(0)
            self.buysellLog +='%s, %s' % (dt.isoformat(), txt)

    def __init__(self):
        # 交易日志
        self.buysellLog = ""

        # 每日收盘价
        self.dataclose = self.datas[0].close

        # 订单
        self.order = None

        self.buyprice = 0
        self.buycomm = 0
        self.buytime = 0

        #10日、60日均线
        self.SAM10 = btind.MovingAverageSimple(self.dataclose(0),period=self.params.maperiod1,subplot=False,plotname=str(self.params.maperiod1)+'日均线')
        self.SAM60 = btind.MovingAverageSimple(self.dataclose(0), period=self.params.maperiod2,subplot=False,plotname=str(self.params.maperiod2)+'日均线')
        # 均线交叉
        self.Crossover = btind.CrossOver(self.SAM10, self.SAM60,plotname='双均线交叉')

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
        if self.Crossover > 0 :
            # 买入总资产30%
            self.newstake = self.broker.getvalue() *0.3/ self.dataclose[0]
            self.newstake = int(self.newstake / 100) * 100
            self.sizer.p.stake = self.newstake
            self.buytime+=1
            self.order = self.buy()
            # 出场
        elif self.Crossover < 0 and self.buytime > 0:
            self.order = self.sell()
            self.buytime = 0
    def stop(self):
        self.log('(短期均线 %2d日 , 长期均线 %2d日) 最终总资产 %.2f\n' %
                 (self.params.maperiod1,self.params.maperiod2, self.broker.getvalue()), doprint=True)