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

from ibapi.object_implem import Object
from ibapi.const import UNSET_DECIMAL
from ibapi.const import UNSET_INTEGER
from ibapi.utils import decimalMaxString
from ibapi.utils import intMaxString
from ibapi.utils import floatMaxString
from ibapi.utils import longMaxString
from ibapi.utils import getEnumTypeName
from enum import Enum

class Execution(Object):
    def __init__(self):
        self.execId = ""
        self.time = ""
        self.acctNumber = ""
        self.exchange = ""
        self.side = ""
        self.shares = UNSET_DECIMAL
        self.price = 0.0
        self.permId = 0
        self.clientId = 0
        self.orderId = 0
        self.liquidation = 0
        self.cumQty = UNSET_DECIMAL
        self.avgPrice = 0.0
        self.orderRef = ""
        self.evRule = ""
        self.evMultiplier = 0.0
        self.modelCode = ""
        self.lastLiquidity = 0
        self.pendingPriceRevision = False
        self.submitter = ""
        self.optExerciseOrLapseType = OptionExerciseType.NoneItem

    def __str__(self):
        return (
            "ExecId: %s, Time: %s, Account: %s, Exchange: %s, Side: %s, Shares: %s, Price: %s, PermId: %s, "
            "ClientId: %s, OrderId: %s, Liquidation: %s, CumQty: %s, AvgPrice: %s, OrderRef: %s, EvRule: %s, "
            "EvMultiplier: %s, ModelCode: %s, LastLiquidity: %s, PendingPriceRevision: %s, Submitter: %s, OptExerciseOrLapseType: %s"
            % (
                self.execId,
                self.time,
                self.acctNumber,
                self.exchange,
                self.side,
                decimalMaxString(self.shares),
                floatMaxString(self.price),
                longMaxString(self.permId),
                intMaxString(self.clientId),
                intMaxString(self.orderId),
                intMaxString(self.liquidation),
                decimalMaxString(self.cumQty),
                floatMaxString(self.avgPrice),
                self.orderRef,
                self.evRule,
                floatMaxString(self.evMultiplier),
                self.modelCode,
                intMaxString(self.lastLiquidity),
                self.pendingPriceRevision,
                self.submitter,
                getEnumTypeName(OptionExerciseType, self.optExerciseOrLapseType),
            )
        )


class ExecutionFilter(Object):
    # Filter fields
    def __init__(self):
        self.clientId = 0
        self.acctCode = ""
        self.time = ""
        self.symbol = ""
        self.secType = ""
        self.exchange = ""
        self.side = ""
        self.lastNDays = UNSET_INTEGER
        self.specificDates = None

class OptionExerciseType(Enum):
    NoneItem = (-1, "None")
    Exercise = (1, "Exercise")
    Lapse = (2, "Lapse")
    DoNothing = (3, "DoNothing")
    Assigned = (100, "Assigned ")
    AutoexerciseClearing = (101, "AutoexerciseClearing")
    Expired = (102, "Expired")
    Netting = (103, "Netting")
    AutoexerciseTrading = (200, "AutoexerciseTrading")

