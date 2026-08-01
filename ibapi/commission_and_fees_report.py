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
from ibapi.utils import intMaxString
from ibapi.utils import floatMaxString


class CommissionAndFeesReport(Object):
    def __init__(self):
        self.execId = ""
        self.commissionAndFees = 0.0
        self.currency = ""
        self.realizedPNL = 0.0
        self.yield_ = 0.0
        self.yieldRedemptionDate = 0  # YYYYMMDD format

    def __str__(self):
        return (
            "ExecId: %s, CommissionAndFees: %s, Currency: %s, RealizedPnL: %s, Yield: %s, YieldRedemptionDate: %s"
            % (
                self.execId,
                floatMaxString(self.commissionAndFees),
                self.currency,
                floatMaxString(self.realizedPNL),
                floatMaxString(self.yield_),
                intMaxString(self.yieldRedemptionDate),
            )
        )
