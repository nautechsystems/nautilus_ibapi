"""
Python TWS API Client

Copyright (C) 2013-2026  Interactive Brokers LLC

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import unittest

from ibapi.order_condition import *


class ConditionOrderTestCase(unittest.TestCase):
    conds = [
        VolumeCondition(8314, "SMART", True, 1000000).And(),
        PercentChangeCondition(1111, "AMEX", True, 0.25).Or(),
        PriceCondition(
            PriceCondition.TriggerMethodEnum.DoubleLast, 2222, "NASDAQ", False, 4.75
        ).And(),
        TimeCondition(True, "20170101 09:30:00").And(),
        MarginCondition(False, 200000).Or(),
        ExecutionCondition("STK", "SMART", "AMD"),
    ]

    for cond in conds:
        print(cond, OrderCondition.__str__(cond))


if "__main__" == __name__:
    unittest.main()
