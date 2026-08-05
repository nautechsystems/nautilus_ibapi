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
from ibapi.utils import setattr_log


class UtilsTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_enum(self):
        e = Enum("ZERO", "ONE", "TWO")
        print(e.ZERO)
        print(e.toStr(e.ZERO))

    def test_setattr_log(self):
        class A:
            def __init__(self):
                self.n = 5

        A.__setattr__ = setattr_log
        a = A()
        print(a.n)
        a.n = 6
        print(a.n)

    def test_polymorphism(self):
        class A:
            def __init__(self):
                self.n = 5

            def m(self):
                self.n += 1

        class B(A):
            def m(self):
                self.n += 2

        o = B()
        print(o)
        # import code; code.interact(local=locals())


if "__main__" == __name__:
    unittest.main()
