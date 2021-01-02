#
#
# 回测函数
#
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from MyStrategy import *
import sys
import backtrader as bt
# 字典：_STRATS、_PARAMS
# _STRATS:{策略名:策略类} eg.{"双均线策略":StrategyOne}
# _PARAMS:{策略名:策略参数字典} eg.{"双均线策略":{"maperiod1":range(5,15),"maperiod2":[55,60,65]}}
_STRATS = {}
_PARAMS = {}
#读取文件生成_STRATS、_PARAMS字典
with open("./MyStrategy/datas/StrategyList.csv", 'r', encoding='gbk') as f:
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

# 回测主体
def start(Strategy,datapath,code,setcash=100.0,comm=0.0):
    # 构建回测架构实体
    cerebro = bt.Cerebro()

    #添加策略
    try:
        cerebro.optstrategy(_STRATS[Strategy],**_PARAMS[Strategy])
    except KeyError:
        raise

    #创建数据反馈
    data = MyCSVData(
        dataname=datapath,
        name=code
    )

    # 添加数据反馈到回测实体
    cerebro.adddata(data)

    # 设置初始资金
    cerebro.broker.setcash(setcash)

    #根据股本加入资金
    cerebro.addsizer(SizerOne)

    #设置手续费
    cerebro.broker.setcommission(commission=comm)

    #设置分析器
    cerebro.addanalyzer(bt.analyzers.Returns, _name='returns')

    #回测运行
    try:
        results = cerebro.run(optreturn=False)
    except IndexError:
        raise

    #回测结果列表[[收益率(float),使用策略(策略类)],...]
    resultList = []
    for i, result in enumerate(results):
        resultList.append([result[0].analyzers.returns.get_analysis()['rtot'], result[0]])
    # rtot: 总收益率
    #
    # ravg: 平均收益率
    #
    # rnorm: 年收益率
    #
    # rnorm100: 年收益率百分比形式

    # 返回策略参数字典、回测结果列表、回测实体(用于绘图)
    return _PARAMS[Strategy],resultList,cerebro


