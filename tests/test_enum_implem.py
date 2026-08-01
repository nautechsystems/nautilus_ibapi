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

from ibapi.enum_implem import Enum


class EnumTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_enum(self):
        e = Enum("ZERO", "ONE", "TWO")
        print(e.ZERO)
        print(e.toStr(e.ZERO))


if "__main__" == __name__:
    unittest.main()
