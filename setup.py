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

# from distutils.core import setup
from setuptools import setup
from ibapi import get_version_string

import sys

if sys.version_info < (3, 1):
    sys.exit("Only Python 3.1 and greater is supported")

setup(
    name="ibapi",
    version=get_version_string(),
    packages=["ibapi","ibapi/protobuf"],
    install_requires=["protobuf==5.29.5"],
    url="https://interactivebrokers.github.io/tws-api",
    license="IB API Non-Commercial License or the IB API Commercial License",
    author="IBG LLC",
    author_email="api@interactivebrokers.com",
    description="Python IB API",
)
