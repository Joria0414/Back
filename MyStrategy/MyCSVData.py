#
# 回测读取数据重写
#
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt

class MyCSVData(bt.feeds.GenericCSVData):
    params = (
        ('nullvalue', float('NaN')),
        ('dtformat', '%Y-%m-%d'),
        ('tmformat', '%H:%M:%S'),

        ('datetime', 0),
        ('time', -1),
        ('open', 6),
        ('high', 4),
        ('low', 5),
        ('close', 3),
        ('volume', 11),
        ('openinterest', -1),
    )