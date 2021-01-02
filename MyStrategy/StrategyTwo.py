# 海龟交易策略
#
# Donchian channel
#
# 上阻力线：过去N天当日最高价的最大值，Max(最高价，N)
#
# 下支撑线：过去M天当日最低价的最小值，Min(最低价，M)
#
# 中心线：(上阻力线 + 下支撑线) / 2
# #####################################################
# 真实波动AR
#
# 真实波幅： 是以下三个值中的最大值：
#
# (1) 当前交易日最高价和最低价的波幅；
#
# (2) 前一交易日的收盘价与当前交易日最高价的波幅；
#
# (3) 前一交易日的收盘价与当前交易日最低价的波幅。
#
# TrueRange（TR）=Max(High−Low,High−PreClose,PreClose−Low)
# #########################################################
# 真实波动幅度均值ATR(N值）
#
# ATR=SMA(TR,N)，即对真实波幅TR进行N日移动平均计算。
# ###################################################
# 建仓单位：Unit=(1%∗账户总资金)/ATR
#
# 建仓单位的意义就是，让一个N值的波动与你总资金1%的波动对应，如果买入1unit单位的资产，当天震幅使得总资产的变化不超过1%。
#
# 具体策略
# 入场：最新价格为20日价格高点，买入一单元股票
# 加仓：最新价格>上一次买入价格+0.5*ATR，买入一单元股票，最多3次加仓
# 出场：最新价格为10日价格低点，清空仓位
# 止损：最新价格<上一次买入价格-2*ATR，清空仓位

#
#
#
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt
import backtrader.indicators as btind

class StrategyTwo(bt.Strategy):
    params =(
        ('maperiod1', 20),
        ('maperiod2', 10),
        ('printlog',True),
    )

    def log(self, txt, dt=None,doprint=False):
        #日志
        if self.params.printlog or doprint:
            dt = dt or self.datas[0].datetime.date(0)
            self.buysellLog += '%s, %s' % (dt.isoformat(), txt)
    def __init__(self):
        self.buysellLog = ""
        #收盘价、最高价、最低价
        self.dataclose = self.datas[0].close
        self.datahigh = self.datas[0].high
        self.datalow = self.datas[0].low

        self.order = None
        self.buyprice = 0
        self.buycomm = 0
        self.newstake = 0
        self.buytime = 0

        #Donchian channel上下线参数计算（上20，下10）
        self.DonchianHi = btind.Highest(self.datahigh(-1),period=self.params.maperiod1,subplot=False,plotname='上阻力线')
        self.DonchianLo = btind.Lowest(self.datalow(-1), period=self.params.maperiod2,subplot=False,plotname='下支撑线')
        #TR、ATR
        self.TR = btind.Max(self.datahigh-self.datalow,abs(self.datahigh-self.dataclose(-1)),abs(self.dataclose(-1)-self.datalow))
        self.ATR = btind.SimpleMovingAverage(self.TR, period=14, subplot=True,plotname='真实波动幅度均值')
        # Donchian channel上轨突破、下轨突破
        self.CrossoverHi = btind.CrossOver(self.dataclose(0), self.DonchianHi,plotname='上阻力线交叉')
        self.CrossoverLo = btind.CrossOver(self.dataclose(0), self.DonchianLo,plotname='下支撑线交叉')

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
        if self.CrossoverHi > 0 and self.buytime == 0:
            self.newstake = self.broker.getvalue() * 0.01 / self.ATR
            self.newstake = int(self.newstake / 100) * 100
            self.sizer.p.stake = self.newstake
            self.buytime = 1
            self.order = self.buy()
            # 加仓
        elif self.datas[0].close > self.buyprice + 0.5 * self.ATR[0] and self.buytime > 0 and self.buytime < 5:
            self.newstake = self.broker.getvalue() * 0.01 / self.ATR
            self.newstake = int(self.newstake / 100) * 100
            self.sizer.p.stake = self.newstake
            self.order = self.buy()
            self.buytime = self.buytime + 1
            # 出场
        elif self.CrossoverLo < 0 and self.buytime > 0:
            self.order = self.sell()
            self.buytime = 0
            # 止损
        elif self.datas[0].close < (self.buyprice - 2 * self.ATR[0]) and self.buytime > 0:
            self.order = self.sell()
            self.buytime = 0
    def stop(self):
        self.log('(上阻力线 %2d日 , 下支撑线 %2d日) 最终总资产 %.2f\n' %
                 (self.params.maperiod1,self.params.maperiod2, self.broker.getvalue()), doprint=True)