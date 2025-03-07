"""
Copyright (C) 2023 Interactive Brokers LLC. All rights reserved. This code is subject to the terms
 and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable.
"""


from ibapi.const import UNSET_INTEGER, UNSET_DECIMAL
from ibapi.enum_implem import Enum
from ibapi.object_implem import Object
from ibapi.utils import floatMaxString, decimalMaxString, intMaxString

TickerId = int
OrderId = int
TagValueList = list

FaDataType = int
FaDataTypeEnum = Enum("N/A", "GROUPS", "N/A", "ALIASES")

MarketDataType = int
MarketDataTypeEnum = Enum("N/A", "REALTIME", "FROZEN", "DELAYED", "DELAYED_FROZEN")

Liquidities = int
LiquiditiesEnum = Enum("None", "Added", "Remove", "RoudedOut")

SetOfString = set
SetOfFloat = set
ListOfOrder = list
ListOfFamilyCode = list
ListOfContractDescription = list
ListOfDepthExchanges = list
ListOfNewsProviders = list
SmartComponentMap = dict
HistogramDataList = list
ListOfPriceIncrements = list
ListOfHistoricalTick = list
ListOfHistoricalTickBidAsk = list
ListOfHistoricalTickLast = list
ListOfHistoricalSessions = list


class BarData(Object):
    def __init__(self):
        self.date = ""
        self.open = 0.0
        self.high = 0.0
        self.low = 0.0
        self.close = 0.0
        self.volume = UNSET_DECIMAL
        self.wap = UNSET_DECIMAL
        self.barCount = 0

    def __str__(self):
        return (
            f"Date: {self.date}, "
            f"Open: {floatMaxString(self.open)}, "
            f"High: {floatMaxString(self.high)}, "
            f"Low: {floatMaxString(self.low)}, "
            f"Close: {floatMaxString(self.close)}, "
            f"Volume: {decimalMaxString(self.volume)}, "
            f"WAP: {decimalMaxString(self.wap)}, "
            f"BarCount: {intMaxString(self.barCount)}"
        )


class RealTimeBar(Object):
    def __init__(
        self,
        time=0,
        endTime=-1,
        open_=0.0,
        high=0.0,
        low=0.0,
        close=0.0,
        volume=UNSET_DECIMAL,
        wap=UNSET_DECIMAL,
        count=0,
    ):
        self.time = time
        self.endTime = endTime
        self.open_ = open_
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.wap = wap
        self.count = count

    def __str__(self):
        return (
            "Time: %s, Open: %s, High: %s, Low: %s, Close: %s, Volume: %s, WAP: %s, Count: %s"
            % (
                intMaxString(self.time),
                floatMaxString(self.open_),
                floatMaxString(self.high),
                floatMaxString(self.low),
                floatMaxString(self.close),
                decimalMaxString(self.volume),
                decimalMaxString(self.wap),
                intMaxString(self.count),
            )
        )


class HistogramData(Object):
    def __init__(self):
        self.price = 0.0
        self.size = UNSET_DECIMAL

    def __str__(self):
        return "Price: %s, Size: %s" % (
            floatMaxString(self.price),
            decimalMaxString(self.size),
        )


class NewsProvider(Object):
    def __init__(self):
        self.code = ""
        self.name = ""

    def __str__(self):
        return f"Code: {self.code}, Name: {self.name}"


class DepthMktDataDescription(Object):
    def __init__(self):
        self.exchange = ""
        self.secType = ""
        self.listingExch = ""
        self.serviceDataType = ""
        self.aggGroup = UNSET_INTEGER

    def __str__(self):
        if self.aggGroup != UNSET_INTEGER:
            aggGroup = self.aggGroup
        else:
            aggGroup = ""
        return (
            "Exchange: %s, SecType: %s, ListingExchange: %s, ServiceDataType: %s, AggGroup: %s, "
            % (
                self.exchange,
                self.secType,
                self.listingExch,
                self.serviceDataType,
                intMaxString(aggGroup),
            )
        )


class SmartComponent(Object):
    def __init__(self):
        self.bitNumber = 0
        self.exchange = ""
        self.exchangeLetter = ""

    def __str__(self):
        return "BitNumber: %d, Exchange: %s, ExchangeLetter: %s" % (
            self.bitNumber,
            self.exchange,
            self.exchangeLetter,
        )


class TickAttrib(Object):
    def __init__(self):
        self.canAutoExecute = False
        self.pastLimit = False
        self.preOpen = False

    def __str__(self):
        return "CanAutoExecute: %d, PastLimit: %d, PreOpen: %d" % (
            self.canAutoExecute,
            self.pastLimit,
            self.preOpen,
        )


class TickAttribBidAsk(Object):
    def __init__(self):
        self.bidPastLow = False
        self.askPastHigh = False

    def __str__(self):
        return "BidPastLow: %d, AskPastHigh: %d" % (self.bidPastLow, self.askPastHigh)


class TickAttribLast(Object):
    def __init__(self):
        self.pastLimit = False
        self.unreported = False

    def __str__(self):
        return "PastLimit: %d, Unreported: %d" % (self.pastLimit, self.unreported)


class FamilyCode(Object):
    def __init__(self):
        self.accountID = ""
        self.familyCodeStr = ""

    def __str__(self):
        return f"AccountId: {self.accountID}, FamilyCodeStr: {self.familyCodeStr}"


class PriceIncrement(Object):
    def __init__(self):
        self.lowEdge = 0.0
        self.increment = 0.0

    def __str__(self):
        return "LowEdge: %s, Increment: %s" % (
            floatMaxString(self.lowEdge),
            floatMaxString(self.increment),
        )


class HistoricalTick(Object):
    def __init__(self):
        self.time = 0
        self.price = 0.0
        self.size = UNSET_DECIMAL

    def __str__(self):
        return "Time: %s, Price: %s, Size: %s" % (
            intMaxString(self.time),
            floatMaxString(self.price),
            decimalMaxString(self.size),
        )


class HistoricalTickBidAsk(Object):
    def __init__(self):
        self.time = 0
        self.tickAttribBidAsk = TickAttribBidAsk()
        self.priceBid = 0.0
        self.priceAsk = 0.0
        self.sizeBid = UNSET_DECIMAL
        self.sizeAsk = UNSET_DECIMAL

    def __str__(self):
        return (
            f"Time: {intMaxString(self.time)}, "
            f"TickAttriBidAsk: {self.tickAttribBidAsk}, "
            f"PriceBid: {floatMaxString(self.priceBid)}, "
            f"PriceAsk: {floatMaxString(self.priceAsk)}, "
            f"SizeBid: {decimalMaxString(self.sizeBid)}, "
            f"SizeAsk: {decimalMaxString(self.sizeAsk)}"
        )


class HistoricalTickLast(Object):
    def __init__(self):
        self.time = 0
        self.tickAttribLast = TickAttribLast()
        self.price = 0.0
        self.size = UNSET_DECIMAL
        self.exchange = ""
        self.specialConditions = ""

    def __str__(self):
        return (
            f"Time: {intMaxString(self.time)}, "
            f"TickAttribLast: {self.tickAttribLast}, "
            f"Price: {floatMaxString(self.price)}, "
            f"Size: {decimalMaxString(self.size)}, "
            f"Exchange: {self.exchange}, "
            f"SpecialConditions: {self.specialConditions}"
        )


class HistoricalSession(Object):
    def __init__(self):
        self.startDateTime = ""
        self.endDateTime = ""
        self.refDate = ""

    def __str__(self):
        return "Start: %s, End: %s, Ref Date: %s" % (
            self.startDateTime,
            self.endDateTime,
            self.refDate,
        )


class WshEventData(Object):
    def __init__(self):
        self.conId = UNSET_INTEGER
        self.filter = ""
        self.fillWatchlist = False
        self.fillPortfolio = False
        self.fillCompetitors = False
        self.startDate = ""
        self.endDate = ""
        self.totalLimit = UNSET_INTEGER

    def __str__(self):
        return (
            f"WshEventData. ConId: {intMaxString(self.conId)}, "
            f"Filter: {self.filter}, "
            f"Fill Watchlist: {self.fillWatchlist:d}, "
            f"Fill Portfolio: {self.fillPortfolio:d}, "
            f"Fill Competitors: {self.fillCompetitors:d}"
        )
