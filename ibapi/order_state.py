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
from ibapi.const import UNSET_DOUBLE, UNSET_DECIMAL
from ibapi.utils import decimalMaxString
from ibapi.utils import floatMaxString

class OrderAllocation(Object):
    def __init__(self):
        self.account = ""
        self.position = UNSET_DECIMAL
        self.positionDesired = UNSET_DECIMAL
        self.positionAfter = UNSET_DECIMAL
        self.desiredAllocQty = UNSET_DECIMAL
        self.allowedAllocQty = UNSET_DECIMAL
        self.isMonetary = False

    def __str__(self):
        s = ("Account: %s, Position: %s, PositionDesired: %s, PositionAfter: %s, "
             "DesiredAllocQty: %s, AllowedAllocQty: %s, IsMonetary: %s") % (
                str(self.account),
                decimalMaxString(self.position),
                decimalMaxString(self.positionDesired),
                decimalMaxString(self.positionAfter),
                decimalMaxString(self.desiredAllocQty),
                decimalMaxString(self.allowedAllocQty),
                str(self.isMonetary),
            )
        return s

class OrderState:
    def __init__(self):
        self.status = ""

        self.initMarginBefore = ""
        self.maintMarginBefore = ""
        self.equityWithLoanBefore = ""
        self.initMarginChange = ""
        self.maintMarginChange = ""
        self.equityWithLoanChange = ""
        self.initMarginAfter = ""
        self.maintMarginAfter = ""
        self.equityWithLoanAfter = ""

        self.commissionAndFees = UNSET_DOUBLE  # type: float
        self.minCommissionAndFees = UNSET_DOUBLE  # type: float
        self.maxCommissionAndFees = UNSET_DOUBLE  # type: float
        self.commissionAndFeesCurrency = ""
        self.marginCurrency = ""
        self.initMarginBeforeOutsideRTH = UNSET_DOUBLE  # type: float
        self.maintMarginBeforeOutsideRTH = UNSET_DOUBLE  # type: float
        self.equityWithLoanBeforeOutsideRTH = UNSET_DOUBLE  # type: float
        self.initMarginChangeOutsideRTH = UNSET_DOUBLE  # type: float
        self.maintMarginChangeOutsideRTH = UNSET_DOUBLE  # type: float
        self.equityWithLoanChangeOutsideRTH = UNSET_DOUBLE  # type: float
        self.initMarginAfterOutsideRTH = UNSET_DOUBLE  # type: float
        self.maintMarginAfterOutsideRTH = UNSET_DOUBLE  # type: float
        self.equityWithLoanAfterOutsideRTH = UNSET_DOUBLE  # type: float
        self.suggestedSize = UNSET_DECIMAL
        self.rejectReason = ""
        self.orderAllocations = None
        self.warningText = ""
        self.completedTime = ""
        self.completedStatus = ""
        
    def __str__(self):
        s = ("Status: %s, InitMarginBefore: %s, MaintMarginBefore: %s, EquityWithLoanBefore: %s, "
             "InitMarginChange: %s, MaintMarginChange: %s, EquityWithLoanChange: %s, "
             "InitMarginAfter: %s, MaintMarginAfter: %s, EquityWithLoanAfter: %s, "
             "CommissionAndFees: %s, MinCommissionAndFees: %s, MaxCommissionAndFees: %s, CommissionAndFeesCurrency: %s, MarginCurrency: %s, "
             "InitMarginBeforeOutsideRTH: %s, MaintMarginBeforeOutsideRTH: %s, EquityWithLoanBeforeOutsideRTH: %s, "
             "InitMarginChangeOutsideRTH: %s, MaintMarginChangeOutsideRTH: %s, equityWithLoanChangeOutsideRTH: %s, "
             "InitMarginAfterOutsideRTH: %s, MaintMarginAfterOutsideRTH: %s, equityWithLoanAfterOutsideRTH: %s, "
             "SuggestedSize: %s, RejectReason: %s, WarningText: %s, CompletedTime: %s, CompletedStatus: %s") % (
                str(self.status),
                str(self.initMarginBefore),
                str(self.maintMarginBefore),
                str(self.equityWithLoanBefore),
                str(self.initMarginChange),
                str(self.maintMarginChange),
                str(self.equityWithLoanChange),
                str(self.initMarginAfter),
                str(self.maintMarginAfter),
                str(self.equityWithLoanAfter),
                floatMaxString(self.commissionAndFees),
                floatMaxString(self.minCommissionAndFees),
                floatMaxString(self.maxCommissionAndFees),
                str(self.commissionAndFeesCurrency),
                str(self.marginCurrency),
                floatMaxString(self.initMarginBeforeOutsideRTH),
                floatMaxString(self.maintMarginBeforeOutsideRTH),
                floatMaxString(self.equityWithLoanBeforeOutsideRTH),
                floatMaxString(self.initMarginChangeOutsideRTH),
                floatMaxString(self.maintMarginChangeOutsideRTH),
                floatMaxString(self.equityWithLoanChangeOutsideRTH),
                floatMaxString(self.initMarginAfterOutsideRTH),
                floatMaxString(self.maintMarginAfterOutsideRTH),
                floatMaxString(self.equityWithLoanAfterOutsideRTH),
                decimalMaxString(self.suggestedSize),
                str(self.rejectReason),
                str(self.warningText),
                str(self.completedTime),
                str(self.completedStatus),
            )
        

        if self.orderAllocations:
            s += " OrderAllocations("
            for orderAllocation in self.orderAllocations:
                s += str(orderAllocation) + "; "
            s += ")"

        return s
        
