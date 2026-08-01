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
import struct
from ibapi import comm


class CommTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_make_msg(self):
        text = "ABCD"
        msg = comm.make_initial_msg(text)

        size = struct.unpack("!I", msg[0:4])[0]

        self.assertEqual(size, len(text), "msg size not good")
        self.assertEqual(msg[4:].decode(), text, "msg payload not good")

    def test_make_field(self):
        text = "ABCD"
        field = comm.make_field(text)

        self.assertEqual(field[-1], "\0", "terminator not good")
        self.assertEqual(len(field[0:-1]), len(text), "payload size not good")
        self.assertEqual(field[0:-1], text, "payload not good")

    def test_read_msg(self):
        text = "ABCD"
        msg = comm.make_initial_msg(text)

        (size, text2, rest) = comm.read_msg(msg)

        self.assertEqual(size, len(text), "msg size not good")
        self.assertEqual(text2.decode(), text, "msg payload not good")
        self.assertEqual(len(rest), 0, "there should be no remainder msg")

    def test_readFields(self):
        text1 = "ABCD"
        text2 = "123"

        msg = comm.make_initial_msg(comm.make_field(text1) + comm.make_field(text2))

        (size, text, rest) = comm.read_msg(msg)
        fields = comm.read_fields(text)

        self.assertEqual(len(fields), 2, "incorrect number of fields")
        self.assertEqual(fields[0].decode(), text1)
        self.assertEqual(fields[1].decode(), text2)


if "__main__" == __name__:
    unittest.main()
