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

"""
Simple class mapping a tag to a value. Both of them are strings. 
They are used in a list to convey extra info with the requests.
"""

from ibapi.object_implem import Object


class TagValue(Object):
    def __init__(self, tag: str = None, value: str = None):
        self.tag = str(tag)
        self.value = str(value)

    def __str__(self):
        # this is not only used for Python dump but when encoding to send
        # so don't change it lightly !
        return f"{self.tag}={self.value};"
