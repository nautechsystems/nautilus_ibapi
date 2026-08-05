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

from ibapi.const import UNSET_INTEGER
from ibapi.object_implem import Object
from ibapi.utils import intMaxString

class OrderCancel(Object):
    def __init__(self):
        self.manualOrderCancelTime = ""
        self.extOperator = ""
        self.manualOrderIndicator = UNSET_INTEGER

    def __str__(self):
        s = "manualOrderCancelTime: %s, extOperator: %s, manualOrderIndicator: %s" % (
            self.manualOrderCancelTime, self.extOperator, intMaxString(self.manualOrderIndicator)
        )

        return s
