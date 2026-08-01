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
Simple class for ineligibility reason 
"""

from ibapi.object_implem import Object

class IneligibilityReason(Object):
    def __init__(self, id_: str = None, description: str = None):
        self.id_ = str(id_)
        self.description = str(description)

    def __str__(self):
        return f"[id: {self.id_}, description: {self.description}];"
