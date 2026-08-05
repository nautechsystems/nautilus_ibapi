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

import logging
from threading import Thread

from ibapi import comm

logger = logging.getLogger(__name__)


class EReader(Thread):
    def __init__(self, conn, msg_queue):
        super().__init__()
        self.conn = conn
        self.msg_queue = msg_queue

    def run(self):
        try:
            logger.debug("EReader thread started")
            buf = b""
            while self.conn.isConnected():
                data = self.conn.recvMsg()
                logger.debug("reader loop, recvd size %d", len(data))
                buf += data

                while len(buf) > 0:
                    (size, msg, buf) = comm.read_msg(buf)
                    # logger.debug("resp %s", buf.decode('ascii'))
                    logger.debug(
                        "size:%d msg.size:%d msg:|%s| buf:%s|", size, len(msg), buf, "|"
                    )

                    if msg:
                        self.msg_queue.put(msg)
                    else:
                        logger.debug("more incoming packet(s) are needed ")
                        break

            logger.debug("EReader thread finished")
        except:
            logger.exception("unhandled exception in EReader thread")
