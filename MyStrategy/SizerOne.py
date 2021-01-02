#
# 买卖股本设置重写
#
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt

class SizerOne(bt.Sizer):
    params = (('stake', 1),)

    def _getsizing(self, comminfo, cash, data, isbuy):
        if isbuy:
            return self.p.stake
        position = self.broker.getposition(data)
        if not position.size:
            return 0
        else:
            return position.size
        return self.p.stakeclass