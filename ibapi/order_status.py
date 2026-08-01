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

from enum import Enum

class OrderStatus(Enum):
    """All possible order status values returned by TWS/Gateway via the
    orderStatus and openOrder callbacks."""

    ApiPending = "ApiPending"
    ApiCancelled = "ApiCancelled"
    PreSubmitted = "PreSubmitted"
    PendingCancel = "PendingCancel"
    Cancelled = "Cancelled"
    Submitted = "Submitted"
    Filled = "Filled"
    Inactive = "Inactive"
    PendingSubmit = "PendingSubmit"
    Unknown = "Unknown"

    def __str__(self) -> str:
        return self.value

    @classmethod
    def get(cls, api_string: str) -> "OrderStatus":
        """Convert a raw TWS/Gateway order status string to the corresponding
        OrderStatus value. Comparison is case-insensitive.
        Returns OrderStatus.Unknown if the string is not recognised."""
        if not api_string:
            return cls.Unknown
        for member in cls:
            if member.value.lower() == api_string.strip().lower():
                return member
        return cls.Unknown

    def is_active(self) -> bool:
        """Returns True if this status indicates the order is still working
        (i.e. further fills or a cancellation are still possible)."""
        return self in (
            OrderStatus.PreSubmitted,
            OrderStatus.PendingCancel,
            OrderStatus.Submitted,
            OrderStatus.PendingSubmit,
        )

    def is_terminal(self) -> bool:
        """Returns True if this status is terminal -- no further fills are expected
        and the order will not transition to another state."""
        return self in (
            OrderStatus.Filled,
            OrderStatus.Cancelled,
            OrderStatus.Inactive,
            OrderStatus.ApiCancelled,
        )
