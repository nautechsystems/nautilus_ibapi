"""
Copyright (C) 2026 Interactive Brokers LLC. All rights reserved. This code is subject to the terms
 and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable.
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
