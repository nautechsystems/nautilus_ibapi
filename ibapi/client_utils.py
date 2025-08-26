"""
Copyright (C) 2025 Interactive Brokers LLC. All rights reserved. This code is subject to the terms
 and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable.
"""

from ibapi.const import UNSET_DOUBLE
from ibapi.execution import ExecutionFilter

from ibapi.contract import Contract, DeltaNeutralContract, ComboLeg
from ibapi.order import Order
from ibapi.order_condition import OrderCondition, OperatorCondition, ContractCondition, PriceCondition, TimeCondition, MarginCondition, ExecutionCondition, VolumeCondition, PercentChangeCondition
from ibapi.tag_value import TagValue
from ibapi.utils import isValidIntValue, isValidFloatValue, isValidLongValue, isValidDecimalValue, decimalMaxString
from ibapi.order_condition import Create

from ibapi.protobuf.ComboLeg_pb2 import ComboLeg as ComboLegProto
from ibapi.protobuf.Contract_pb2 import Contract as ContractProto
from ibapi.protobuf.DeltaNeutralContract_pb2 import DeltaNeutralContract as DeltaNeutralContractProto
from ibapi.protobuf.OrderCancel_pb2 import OrderCancel as OrderCancelProto
from ibapi.protobuf.OrderCondition_pb2 import OrderCondition as OrderConditionProto
from ibapi.protobuf.PlaceOrderRequest_pb2 import PlaceOrderRequest as PlaceOrderRequestProto
from ibapi.protobuf.CancelOrderRequest_pb2 import CancelOrderRequest as CancelOrderRequestProto
from ibapi.protobuf.GlobalCancelRequest_pb2 import GlobalCancelRequest as GlobalCancelRequestProto
from ibapi.protobuf.ExecutionFilter_pb2 import ExecutionFilter as ExecutionFilterProto
from ibapi.protobuf.ExecutionRequest_pb2 import ExecutionRequest as ExecutionRequestProto
from ibapi.protobuf.Order_pb2 import Order as OrderProto
from ibapi.protobuf.SoftDollarTier_pb2 import SoftDollarTier as SoftDollarTierProto

@staticmethod
def createExecutionRequestProto(reqId: int, execFilter: ExecutionFilter) -> ExecutionRequestProto:
    executionFilterProto = ExecutionFilterProto()
    if isValidIntValue(execFilter.clientId): executionFilterProto.clientId = execFilter.clientId
    if execFilter.acctCode: executionFilterProto.acctCode = execFilter.acctCode
    if execFilter.time: executionFilterProto.time = execFilter.time
    if execFilter.symbol: executionFilterProto.symbol = execFilter.symbol
    if execFilter.secType: executionFilterProto.secType = execFilter.secType
    if execFilter.exchange: executionFilterProto.exchange = execFilter.exchange
    if execFilter.side: executionFilterProto.side = execFilter.side
    if isValidIntValue(execFilter.lastNDays): executionFilterProto.lastNDays = execFilter.lastNDays
    if execFilter.specificDates is not None and execFilter.specificDates: executionFilterProto.specificDates.extend(execFilter.specificDates)
    executionRequestProto = ExecutionRequestProto()
    if isValidIntValue(reqId): executionRequestProto.reqId = reqId
    executionRequestProto.executionFilter.CopyFrom(executionFilterProto)
    return executionRequestProto
 
@staticmethod
def createPlaceOrderRequestProto(orderId: int, contract: Contract, order: Order) -> PlaceOrderRequestProto:
    placeOrderRequestProto = PlaceOrderRequestProto()
    if isValidIntValue(orderId): placeOrderRequestProto.orderId = orderId
    contractProto = createContractProto(contract, order)
    if contractProto is not None: placeOrderRequestProto.contract.CopyFrom(contractProto)
    orderProto = createOrderProto(order)
    if orderProto is not None: placeOrderRequestProto.order.CopyFrom(orderProto)
    return placeOrderRequestProto

@staticmethod
def createContractProto(contract: Contract, order: Order) -> ContractProto:
    contractProto = ContractProto()
    if isValidIntValue(contract.conId): contractProto.conId = contract.conId
    if contract.symbol: contractProto.symbol = contract.symbol
    if contract.secType: contractProto.secType = contract.secType
    if contract.lastTradeDateOrContractMonth: contractProto.lastTradeDateOrContractMonth = contract.lastTradeDateOrContractMonth
    if isValidFloatValue(contract.strike): contractProto.strike = contract.strike
    if contract.right: contractProto.right = contract.right
    if contract.multiplier: contractProto.multiplier = float(contract.multiplier)
    if contract.exchange: contractProto.exchange = contract.exchange
    if contract.primaryExchange: contractProto.primaryExchange = contract.primaryExchange
    if contract.currency: contractProto.currency = contract.currency
    if contract.localSymbol: contractProto.localSymbol = contract.localSymbol
    if contract.tradingClass: contractProto.tradingClass = contract.tradingClass
    if contract.secIdType: contractProto.secIdType = contract.secIdType
    if contract.secId: contractProto.secId = contract.secId
    if contract.includeExpired: contractProto.includeExpired = contract.includeExpired
    if contract.comboLegsDescrip: contractProto.comboLegsDescrip = contract.comboLegsDescrip
    if contract.description: contractProto.description = contract.description
    if contract.issuerId: contractProto.issuerId = contract.issuerId

    comboLegProtoList = createComboLegProtoList(contract, order)
    if comboLegProtoList is not None and comboLegProtoList: contractProto.comboLegs.extend(comboLegProtoList)

    deltaNeutralContractProto = createDeltaNeutralContractProto(contract)
    if deltaNeutralContractProto is not None: contractProto.deltaNeutralContract.CopyFrom(deltaNeutralContractProto)

    return contractProto

@staticmethod
def createDeltaNeutralContractProto(contract: Contract) -> DeltaNeutralContractProto:
    deltaNeutralContractProto = None
    if contract.deltaNeutralContract is not None:
        deltaNeutralContract = contract.deltaNeutralContract
        deltaNeutralContractProto = DeltaNeutralContractProto()
        if isValidIntValue(deltaNeutralContract.conId): deltaNeutralContractProto.conId = deltaNeutralContract.conId
        if isValidFloatValue(deltaNeutralContract.delta): deltaNeutralContractProto.delta = deltaNeutralContract.delta
        if isValidFloatValue(deltaNeutralContract.price): deltaNeutralContractProto.price = deltaNeutralContract.price
    return deltaNeutralContractProto


@staticmethod
def createComboLegProtoList(contract: Contract, order: Order) -> list[ComboLegProto]:
    comboLegs = contract.comboLegs
    orderComboLegs = order.orderComboLegs
    comboLegProtoList = []
    if comboLegs is not None and comboLegs:
        for i, comboLeg in enumerate(comboLegs):
            perLegPrice = UNSET_DOUBLE
            if orderComboLegs is not None and i < len(orderComboLegs):
                perLegPrice = orderComboLegs[i].price
            comboLegProto = createComboLegProto(comboLeg, perLegPrice)
            comboLegProtoList.append(comboLegProto)
    return comboLegProtoList

@staticmethod
def createComboLegProto(comboLeg: ComboLeg, perLegPrice: float) -> ComboLegProto:
    comboLegProto = ComboLegProto()
    if isValidIntValue(comboLeg.conId): comboLegProto.conId = comboLeg.conId
    if isValidIntValue(comboLeg.ratio): comboLegProto.ratio = comboLeg.ratio
    if comboLeg.action: comboLegProto.action = comboLeg.action
    if comboLeg.exchange: comboLegProto.exchange = comboLeg.exchange
    if isValidIntValue(comboLeg.openClose): comboLegProto.openClose = comboLeg.openClose
    if isValidIntValue(comboLeg.shortSaleSlot): comboLegProto.shortSalesSlot = comboLeg.shortSaleSlot
    if comboLeg.designatedLocation: comboLegProto.designatedLocation = comboLeg.designatedLocation
    if isValidIntValue(comboLeg.exemptCode): comboLegProto.exemptCode = comboLeg.exemptCode
    if isValidFloatValue(perLegPrice): comboLegProto.perLegPrice = perLegPrice
    return comboLegProto

@staticmethod
def createOrderProto(order: Order) -> OrderProto:
    orderProto = OrderProto()
    if isValidIntValue(order.clientId): order.clientId = order.clientId
    if isValidLongValue(order.permId): orderProto.permId = order.permId
    if isValidIntValue(order.parentId): orderProto.parentId = order.parentId
    if order.action: orderProto.action = order.action
    if isValidDecimalValue(order.totalQuantity): orderProto.totalQuantity = decimalMaxString(order.totalQuantity)
    if isValidIntValue(order.displaySize): orderProto.displaySize = order.displaySize
    if order.orderType: orderProto.orderType = order.orderType
    if isValidFloatValue(order.lmtPrice): orderProto.lmtPrice = order.lmtPrice
    if isValidFloatValue(order.auxPrice): orderProto.auxPrice = order.auxPrice
    if order.tif: orderProto.tif = order.tif
    if order.account: orderProto.account = order.account
    if order.settlingFirm: orderProto.settlingFirm = order.settlingFirm
    if order.clearingAccount: orderProto.clearingAccount = order.clearingAccount
    if order.clearingIntent: orderProto.clearingIntent = order.clearingIntent
    if order.allOrNone: orderProto.allOrNone = order.allOrNone
    if order.blockOrder: orderProto.blockOrder = order.blockOrder
    if order.hidden: orderProto.hidden = order.hidden
    if order.outsideRth: orderProto.outsideRth = order.outsideRth
    if order.sweepToFill: orderProto.sweepToFill = order.sweepToFill
    if isValidFloatValue(order.percentOffset): orderProto.percentOffset = order.percentOffset
    if isValidFloatValue(order.trailingPercent): orderProto.trailingPercent = order.trailingPercent
    if isValidFloatValue(order.trailStopPrice): orderProto.trailStopPrice = order.trailStopPrice
    if isValidIntValue(order.minQty): orderProto.minQty = order.minQty
    if order.goodAfterTime: orderProto.goodAfterTime = order.goodAfterTime
    if order.goodTillDate: orderProto.goodTillDate = order.goodTillDate
    if order.ocaGroup: orderProto.ocaGroup = order.ocaGroup
    if order.orderRef: orderProto.orderRef = order.orderRef
    if order.rule80A: orderProto.rule80A = order.rule80A
    if isValidIntValue(order.ocaType): orderProto.ocaType = order.ocaType
    if isValidIntValue(order.triggerMethod): orderProto.triggerMethod = order.triggerMethod
    if order.activeStartTime: orderProto.activeStartTime = order.activeStartTime
    if order.activeStopTime: orderProto.activeStopTime = order.activeStopTime
    if order.faGroup: orderProto.faGroup = order.faGroup
    if order.faMethod: orderProto.faMethod = order.faMethod
    if order.faPercentage: orderProto.faPercentage = order.faPercentage
    if isValidFloatValue(order.volatility): orderProto.volatility = order.volatility
    if isValidIntValue(order.volatilityType): orderProto.volatilityType = order.volatilityType
    if order.continuousUpdate: orderProto.continuousUpdate = order.continuousUpdate
    if isValidIntValue(order.referencePriceType): orderProto.referencePriceType = order.referencePriceType
    if order.deltaNeutralOrderType: orderProto.deltaNeutralOrderType = order.deltaNeutralOrderType
    if isValidFloatValue(order.deltaNeutralAuxPrice): orderProto.deltaNeutralAuxPrice = order.deltaNeutralAuxPrice
    if isValidIntValue(order.deltaNeutralConId): orderProto.deltaNeutralConId = order.deltaNeutralConId
    if order.deltaNeutralOpenClose: orderProto.deltaNeutralOpenClose = order.deltaNeutralOpenClose
    if order.deltaNeutralShortSale: orderProto.deltaNeutralShortSale = order.deltaNeutralShortSale
    if isValidIntValue(order.deltaNeutralShortSaleSlot): orderProto.deltaNeutralShortSaleSlot = order.deltaNeutralShortSaleSlot
    if order.deltaNeutralDesignatedLocation: orderProto.deltaNeutralDesignatedLocation = order.deltaNeutralDesignatedLocation
    if isValidIntValue(order.scaleInitLevelSize): orderProto.scaleInitLevelSize = order.scaleInitLevelSize
    if isValidIntValue(order.scaleSubsLevelSize): orderProto.scaleSubsLevelSize = order.scaleSubsLevelSize
    if isValidFloatValue(order.scalePriceIncrement): orderProto.scalePriceIncrement = order.scalePriceIncrement
    if isValidFloatValue(order.scalePriceAdjustValue): orderProto.scalePriceAdjustValue = order.scalePriceAdjustValue
    if isValidIntValue(order.scalePriceAdjustInterval): orderProto.scalePriceAdjustInterval = order.scalePriceAdjustInterval
    if isValidFloatValue(order.scaleProfitOffset): orderProto.scaleProfitOffset = order.scaleProfitOffset
    if order.scaleAutoReset: orderProto.scaleAutoReset = order.scaleAutoReset
    if isValidIntValue(order.scaleInitPosition): orderProto.scaleInitPosition = order.scaleInitPosition
    if isValidIntValue(order.scaleInitFillQty): orderProto.scaleInitFillQty = order.scaleInitFillQty
    if order.scaleRandomPercent: orderProto.scaleRandomPercent = order.scaleRandomPercent
    if order.scaleTable: orderProto.scaleTable = order.scaleTable
    if order.hedgeType: orderProto.hedgeType = order.hedgeType
    if order.hedgeParam: orderProto.hedgeParam = order.hedgeParam

    if order.algoStrategy: orderProto.algoStrategy = order.algoStrategy
    fillTagValueList(order.algoParams, orderProto.algoParams)
    if order.algoId: orderProto.algoId = order.algoId

    fillTagValueList(order.smartComboRoutingParams, orderProto.smartComboRoutingParams)

    if order.whatIf: orderProto.whatIf = order.whatIf
    if order.transmit: orderProto.transmit = order.transmit
    if order.overridePercentageConstraints: orderProto.overridePercentageConstraints = order.overridePercentageConstraints
    if order.openClose: orderProto.openClose = order.openClose
    if isValidIntValue(order.origin): orderProto.origin = order.origin
    if isValidIntValue(order.shortSaleSlot): orderProto.shortSaleSlot = order.shortSaleSlot
    if order.designatedLocation: orderProto.designatedLocation = order.designatedLocation
    if isValidIntValue(order.exemptCode): orderProto.exemptCode = order.exemptCode
    if order.deltaNeutralSettlingFirm: orderProto.deltaNeutralSettlingFirm = order.deltaNeutralSettlingFirm
    if order.deltaNeutralClearingAccount: orderProto.deltaNeutralClearingAccount = order.deltaNeutralClearingAccount
    if order.deltaNeutralClearingIntent: orderProto.deltaNeutralClearingIntent = order.deltaNeutralClearingIntent
    if isValidIntValue(order.discretionaryAmt): orderProto.discretionaryAmt = order.discretionaryAmt
    if order.optOutSmartRouting: orderProto.optOutSmartRouting = order.optOutSmartRouting
    if isValidIntValue(order.exemptCode): orderProto.exemptCode = order.exemptCode
    if isValidFloatValue(order.startingPrice): orderProto.startingPrice = order.startingPrice
    if isValidFloatValue(order.stockRefPrice): orderProto.stockRefPrice = order.stockRefPrice
    if isValidFloatValue(order.delta): orderProto.delta = order.delta
    if isValidFloatValue(order.stockRangeLower): orderProto.stockRangeLower = order.stockRangeLower
    if isValidFloatValue(order.stockRangeUpper): orderProto.stockRangeUpper = order.stockRangeUpper
    if order.notHeld: orderProto.notHeld = order.notHeld

    fillTagValueList(order.orderMiscOptions, orderProto.orderMiscOptions)

    if order.solicited: orderProto.solicited = order.solicited
    if order.randomizeSize: orderProto.randomizeSize = order.randomizeSize
    if order.randomizePrice: orderProto.randomizePrice = order.randomizePrice
    if isValidIntValue(order.referenceContractId): orderProto.referenceContractId = order.referenceContractId
    if isValidFloatValue(order.peggedChangeAmount): orderProto.peggedChangeAmount = order.peggedChangeAmount
    if order.isPeggedChangeAmountDecrease: orderProto.isPeggedChangeAmountDecrease = order.isPeggedChangeAmountDecrease
    if isValidFloatValue(order.referenceChangeAmount): orderProto.referenceChangeAmount = order.referenceChangeAmount
    if order.referenceExchangeId: orderProto.referenceExchangeId = order.referenceExchangeId
    if order.adjustedOrderType: orderProto.adjustedOrderType = order.adjustedOrderType
    if isValidFloatValue(order.triggerPrice): orderProto.triggerPrice = order.triggerPrice
    if isValidFloatValue(order.adjustedStopPrice): orderProto.adjustedStopPrice = order.adjustedStopPrice
    if isValidFloatValue(order.adjustedStopLimitPrice): orderProto.adjustedStopLimitPrice = order.adjustedStopLimitPrice
    if isValidFloatValue(order.adjustedTrailingAmount): orderProto.adjustedTrailingAmount = order.adjustedTrailingAmount
    if isValidIntValue(order.adjustableTrailingUnit): orderProto.adjustableTrailingUnit = order.adjustableTrailingUnit
    if isValidFloatValue(order.lmtPriceOffset): orderProto.lmtPriceOffset = order.lmtPriceOffset

    orderConditionList = createConditionsProto(order)
    if orderConditionList is not None and orderConditionList: orderProto.conditions.extend(orderConditionList)
    if order.conditionsCancelOrder: orderProto.conditionsCancelOrder = order.conditionsCancelOrder
    if order.conditionsIgnoreRth: orderProto.conditionsIgnoreRth = order.conditionsIgnoreRth

    if order.modelCode: orderProto.modelCode = order.modelCode
    if order.extOperator: orderProto.extOperator = order.extOperator

    softDollarTier = createSoftDollarTierProto(order)
    if softDollarTier is not None: orderProto.softDollarTier.CopyFrom(softDollarTier)

    if isValidFloatValue(order.cashQty): orderProto.cashQty = order.cashQty
    if order.mifid2DecisionMaker: orderProto.mifid2DecisionMaker = order.mifid2DecisionMaker
    if order.mifid2DecisionAlgo: orderProto.mifid2DecisionAlgo = order.mifid2DecisionAlgo
    if order.mifid2ExecutionTrader: orderProto.mifid2ExecutionTrader = order.mifid2ExecutionTrader
    if order.mifid2ExecutionAlgo: orderProto.mifid2ExecutionAlgo = order.mifid2ExecutionAlgo
    if order.dontUseAutoPriceForHedge: orderProto.dontUseAutoPriceForHedge = order.dontUseAutoPriceForHedge
    if order.isOmsContainer: orderProto.isOmsContainer = order.isOmsContainer
    if order.discretionaryUpToLimitPrice: orderProto.discretionaryUpToLimitPrice = order.discretionaryUpToLimitPrice
    if order.usePriceMgmtAlgo is not None: orderProto.usePriceMgmtAlgo = 1 if order.usePriceMgmtAlgo else 0
    if isValidIntValue(order.duration): orderProto.duration = order.duration
    if isValidIntValue(order.postToAts): orderProto.postToAts = order.postToAts
    if order.advancedErrorOverride: orderProto.advancedErrorOverride = order.advancedErrorOverride
    if order.manualOrderTime: orderProto.manualOrderTime = order.manualOrderTime
    if isValidIntValue(order.minTradeQty): orderProto.minTradeQty = order.minTradeQty
    if isValidIntValue(order.minCompeteSize): orderProto.minCompeteSize = order.minCompeteSize
    if isValidFloatValue(order.competeAgainstBestOffset): orderProto.competeAgainstBestOffset = order.competeAgainstBestOffset
    if isValidFloatValue(order.midOffsetAtWhole): orderProto.midOffsetAtWhole = order.midOffsetAtWhole
    if isValidFloatValue(order.midOffsetAtHalf): orderProto.midOffsetAtHalf = order.midOffsetAtHalf
    if order.customerAccount: orderProto.customerAccount = order.customerAccount
    if order.professionalCustomer: orderProto.professionalCustomer = order.professionalCustomer
    if order.bondAccruedInterest: orderProto.bondAccruedInterest = order.bondAccruedInterest
    if order.includeOvernight: orderProto.includeOvernight = order.includeOvernight
    if isValidIntValue(order.manualOrderIndicator): orderProto.manualOrderIndicator = order.manualOrderIndicator
    if order.submitter: orderProto.submitter = order.submitter
    if order.autoCancelParent: orderProto.autoCancelParent = order.autoCancelParent
    if order.imbalanceOnly: orderProto.imbalanceOnly = order.imbalanceOnly

    return orderProto

def createConditionsProto(order: Order) -> list[OrderConditionProto]:
    orderConditionProtoList = []
    if order.conditions is not None and order.conditions:
        for orderCondition in order.conditions:
            conditionType = orderCondition.condType

            if OrderCondition.Price == conditionType:
                orderConditionProto = createPriceConditionProto(orderCondition)
            elif OrderCondition.Time == conditionType:
                orderConditionProto = createTimeConditionProto(orderCondition)
            elif OrderCondition.Margin == conditionType:
                orderConditionProto = createMarginConditionProto(orderCondition)
            elif OrderCondition.Execution == conditionType:
                orderConditionProto = createExecutionConditionProto(orderCondition)
            elif OrderCondition.Volume == conditionType:
                orderConditionProto = createVolumeConditionProto(orderCondition)
            elif OrderCondition.PercentChange == conditionType:
                orderConditionProto = createPercentChangeConditionProto(orderCondition)

            if orderConditionProto is not None: orderConditionProtoList.append(orderConditionProto)

    return orderConditionProtoList

@staticmethod
def createOrderConditionProto(orderCondition: OrderCondition) -> OrderConditionProto:
    conditionType = orderCondition.condType
    isConjunctionConnection = orderCondition.isConjunctionConnection
    orderConditionProto = OrderConditionProto()
    if isValidIntValue(conditionType): orderConditionProto.type = conditionType
    orderConditionProto.isConjunctionConnection = isConjunctionConnection
    return orderConditionProto

@staticmethod
def createOperatorConditionProto(operatorCondition: OperatorCondition) -> OrderConditionProto:
    orderConditionProto = createOrderConditionProto(operatorCondition)
    operatorConditionProto = OrderConditionProto()
    operatorConditionProto.MergeFrom(orderConditionProto)
    operatorConditionProto.isMore = operatorCondition.isMore
    return operatorConditionProto

@staticmethod
def createContractConditionProto(contractCondition: ContractCondition) -> OrderConditionProto:
    operatorConditionProto = createOperatorConditionProto(contractCondition)
    contractConditionProto = OrderConditionProto()
    contractConditionProto.MergeFrom(operatorConditionProto)
    if isValidIntValue(contractCondition.conId): contractConditionProto.conId = contractCondition.conId
    if contractCondition.exchange: contractConditionProto.exchange = contractCondition.exchange
    return contractConditionProto

@staticmethod
def createPriceConditionProto(priceCondition: PriceCondition) -> OrderConditionProto:
    contractConditionProto = createContractConditionProto(priceCondition)
    priceConditionProto = OrderConditionProto()
    priceConditionProto.MergeFrom(contractConditionProto)
    if isValidFloatValue(priceCondition.price): priceConditionProto.price = priceCondition.price
    if isValidIntValue(priceCondition.triggerMethod): priceConditionProto.triggerMethod = priceCondition.triggerMethod
    return priceConditionProto

@staticmethod
def createTimeConditionProto(timeCondition: TimeCondition) -> OrderConditionProto:
    operatorConditionProto = createOperatorConditionProto(timeCondition)
    timeConditionProto = OrderConditionProto()
    timeConditionProto.MergeFrom(operatorConditionProto)
    if timeCondition.time: timeConditionProto.time = timeCondition.time
    return timeConditionProto

@staticmethod
def createMarginConditionProto(marginCondition: MarginCondition) -> OrderConditionProto:
    operatorConditionProto = createOperatorConditionProto(marginCondition)
    marginConditionProto = OrderConditionProto()
    marginConditionProto.MergeFrom(operatorConditionProto)
    if isValidFloatValue(marginCondition.percent): marginConditionProto.percent = marginCondition.percent
    return marginConditionProto

@staticmethod
def createExecutionConditionProto(executionCondition: ExecutionCondition) -> OrderConditionProto:
    orderConditionProto = createOrderConditionProto(executionCondition)
    executionConditionProto = OrderConditionProto()
    executionConditionProto.MergeFrom(orderConditionProto)
    if executionCondition.secType: executionConditionProto.secType = executionCondition.secType
    if executionCondition.exchange: executionConditionProto.exchange = executionCondition.exchange
    if executionCondition.symbol: executionConditionProto.symbol = executionCondition.symbol
    return executionConditionProto

@staticmethod
def createVolumeConditionProto(volumeCondition: VolumeCondition) -> OrderConditionProto:
    contractConditionProto = createContractConditionProto(volumeCondition)
    volumeConditionProto = OrderConditionProto()
    volumeConditionProto.MergeFrom(contractConditionProto)
    if isValidIntValue(volumeCondition.volume): volumeConditionProto.volume = volumeCondition.volume
    return volumeConditionProto

@staticmethod
def createPercentChangeConditionProto(percentChangeCondition: PercentChangeCondition) -> OrderConditionProto:
    contractConditionProto = createContractConditionProto(percentChangeCondition)
    percentChangeConditionProto = OrderConditionProto()
    percentChangeConditionProto.MergeFrom(contractConditionProto)
    if isValidFloatValue(percentChangeCondition.changePercent): percentChangeConditionProto.changePercent = percentChangeCondition.changePercent
    return percentChangeConditionProto

@staticmethod
def createSoftDollarTierProto(order: Order) -> SoftDollarTierProto:
    softDollarTierProto = None
    tier = order.softDollarTier
    if tier is not None:
        softDollarTierProto = SoftDollarTierProto()
        if tier.name: softDollarTierProto.name = tier.name
        if tier.val: softDollarTierProto.value = tier.val
        if tier.displayName: softDollarTierProto.displayName = tier.displayName
    return softDollarTierProto

@staticmethod
def fillTagValueList(tagValueList: list, orderProtoMap: dict):
    if tagValueList is not None and tagValueList:
        for tagValue in tagValueList: 
            orderProtoMap[tagValue.tag] = tagValue.value

@staticmethod
def createCancelOrderRequestProto(orderId: int, orderCancel: OrderCancelProto) -> CancelOrderRequestProto:
    cancelOrderRequestProto = CancelOrderRequestProto()
    if isValidIntValue(orderId): cancelOrderRequestProto.orderId = orderId
    orderCancelProto = createOrderCancelProto(orderCancel)
    if orderCancelProto is not None: cancelOrderRequestProto.orderCancel.CopyFrom(orderCancelProto)
    return cancelOrderRequestProto

@staticmethod
def createGlobalCancelRequestProto(orderCancel: OrderCancelProto) -> GlobalCancelRequestProto:
    globalCancelRequestProto = GlobalCancelRequestProto()
    orderCancelProto = createOrderCancelProto(orderCancel)
    if orderCancelProto is not None: globalCancelRequestProto.orderCancel.CopyFrom(orderCancelProto)
    return globalCancelRequestProto

@staticmethod
def createOrderCancelProto(orderCancel: OrderCancelProto) -> OrderCancelProto:
    orderCancelProto = OrderCancelProto()
    if orderCancel.manualOrderCancelTime: orderCancelProto.manualOrderCancelTime = orderCancel.manualOrderCancelTime
    if orderCancel.extOperator: orderCancelProto.extOperator = orderCancel.extOperator
    if isValidIntValue(orderCancel.manualOrderIndicator): orderCancelProto.manualOrderIndicator = orderCancel.manualOrderIndicator
    return orderCancelProto
