"""
Copyright (C) 2025 Interactive Brokers LLC. All rights reserved. This code is subject to the terms
 and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable.
"""
from decimal import Decimal

from ibapi.contract import ComboLeg, Contract, DeltaNeutralContract
from ibapi.execution import Execution, OptionExerciseType
from ibapi.order import Order, OrderComboLeg
from ibapi.order_condition import OrderCondition, OperatorCondition, ContractCondition, PriceCondition, TimeCondition, MarginCondition, ExecutionCondition, VolumeCondition, PercentChangeCondition
from ibapi.order_state import OrderState, OrderAllocation
from ibapi.softdollartier import SoftDollarTier
from ibapi.tag_value import TagValue
from ibapi.utils import floatMaxString, getEnumTypeFromString, decimalMaxString

#from ibapi.protobuf.ComboLeg_pb2 import ComboLeg as ComboLegProto
from ibapi.protobuf.Contract_pb2 import Contract as ContractProto
from ibapi.protobuf.DeltaNeutralContract_pb2 import DeltaNeutralContract as DeltaNeutralContractProto
from ibapi.protobuf.Execution_pb2 import Execution as ExecutionProto
from ibapi.protobuf.Order_pb2 import Order as OrderProto
from ibapi.protobuf.OrderCondition_pb2 import OrderCondition as OrderConditionProto
from ibapi.protobuf.OrderState_pb2 import OrderState as OrderStateProto
from ibapi.protobuf.OrderAllocation_pb2 import OrderAllocation as OrderAllocatiionProto
from ibapi.protobuf.SoftDollarTier_pb2 import SoftDollarTier as SoftDollarTierProto

@staticmethod
def decodeContract(contractProto: ContractProto) -> Contract:
    contract = Contract()
    if contractProto.HasField('conId'): contract.conId = contractProto.conId
    if contractProto.HasField('symbol'): contract.symbol = contractProto.symbol
    if contractProto.HasField('secType'): contract.secType = contractProto.secType
    if contractProto.HasField('lastTradeDateOrContractMonth'): contract.lastTradeDateOrContractMonth = contractProto.lastTradeDateOrContractMonth
    if contractProto.HasField('strike'): contract.strike = contractProto.strike
    if contractProto.HasField('right'): contract.right = contractProto.right
    if contractProto.HasField('multiplier'): contract.multiplier = floatMaxString(contractProto.multiplier)
    if contractProto.HasField('exchange'): contract.exchange = contractProto.exchange
    if contractProto.HasField('currency'): contract.currency = contractProto.currency
    if contractProto.HasField('localSymbol'): contract.localSymbol = contractProto.localSymbol
    if contractProto.HasField('tradingClass'): contract.tradingClass = contractProto.tradingClass
    if contractProto.HasField('comboLegsDescrip'): contract.comboLegsDescrip = contractProto.comboLegsDescrip

    comboLegs = decodeComboLegs(contractProto)
    if comboLegs is not None and comboLegs: contract.comboLegs = comboLegs

    deltaNeutralContract = decodeDeltaNeutralContract(contractProto)
    if deltaNeutralContract is not None: contract.deltaNeutralContract = deltaNeutralContract

    return contract

@staticmethod
def decodeComboLegs(contractProto: ContractProto) -> list[ComboLeg]:
    comboLegs = []
    comboLegProtoList = contractProto.comboLegs
    if comboLegProtoList:
        for comboLegProto in comboLegProtoList:
            comboLeg = ComboLeg()
            if comboLegProto.HasField('conId'): comboLeg.conId = comboLegProto.conId
            if comboLegProto.HasField('ratio'): comboLeg.ratio = comboLegProto.ratio
            if comboLegProto.HasField('action'): comboLeg.action = comboLegProto.action
            if comboLegProto.HasField('exchange'): comboLeg.exchange = comboLegProto.exchange
            if comboLegProto.HasField('openClose'): comboLeg.openClose = comboLegProto.openClose
            if comboLegProto.HasField('shortSalesSlot'): comboLeg.shortSalesSlot = comboLegProto.shortSalesSlot
            if comboLegProto.HasField('designatedLocation'): comboLeg.designatedLocation = comboLegProto.designatedLocation
            if comboLegProto.HasField('exemptCode'): comboLeg.exemptCode = comboLegProto.exemptCode
            comboLegs.append(comboLeg)

    return comboLegs

@staticmethod
def decodeOrderComboLegs(contractProto: ContractProto) -> list[OrderComboLeg]:
    orderComboLegs = []
    comboLegProtoList = contractProto.comboLegs
    if comboLegProtoList:
        for comboLegProto in comboLegProtoList:
            orderComboLeg = OrderComboLeg()
            if comboLegProto.HasField('perLegPrice'): orderComboLeg.price = comboLegProto.perLegPrice
            orderComboLegs.append(orderComboLeg)

    return orderComboLegs

@staticmethod
def decodeDeltaNeutralContract(contractProto: ContractProto) -> DeltaNeutralContract:
    deltaNeutralContract = None
    deltaNeutralContractProto = DeltaNeutralContractProto()
    if contractProto.HasField('deltaNeutralContract'): deltaNeutralContractProto.CopyFrom(contractProto.deltaNeutralContract)
    if deltaNeutralContractProto is not None: 
        deltaNeutralContract = DeltaNeutralContract()
        if (deltaNeutralContractProto.HasField('conId')): deltaNeutralContract.conId = deltaNeutralContractProto.conId
        if (deltaNeutralContractProto.HasField('delta')): deltaNeutralContract.delta = deltaNeutralContractProto.delta
        if (deltaNeutralContractProto.HasField('price')): deltaNeutralContract.price = deltaNeutralContractProto.price

    return deltaNeutralContract

@staticmethod
def decodeExecution(executionProto: ExecutionProto) -> Execution:
    execution = Execution()
    if executionProto.HasField('orderId'): execution.orderId = executionProto.orderId
    if executionProto.HasField('clientId'): execution.clientId = executionProto.clientId
    if executionProto.HasField('execId'): execution.execId = executionProto.execId
    if executionProto.HasField('time'): execution.time = executionProto.time
    if executionProto.HasField('acctNumber'): execution.acctNumber = executionProto.acctNumber
    if executionProto.HasField('exchange'): execution.exchange = executionProto.exchange
    if executionProto.HasField('side'): execution.side = executionProto.side
    if executionProto.HasField('shares'): execution.shares = Decimal(executionProto.shares)
    if executionProto.HasField('price'): execution.price = executionProto.price
    if executionProto.HasField('permId'): execution.permId = executionProto.permId
    if executionProto.HasField('isLiquidation'): execution.liquidation = 1 if executionProto.isLiquidation else 0
    if executionProto.HasField('cumQty'): execution.cumQty = Decimal(executionProto.cumQty)
    if executionProto.HasField('avgPrice'): execution.avgPrice = executionProto.avgPrice
    if executionProto.HasField('orderRef'): execution.orderRef = executionProto.orderRef
    if executionProto.HasField('evRule'): execution.evRule = executionProto.evRule
    if executionProto.HasField('evMultiplier'): execution.evMultiplier = executionProto.evMultiplier
    if executionProto.HasField('modelCode'): execution.modelCode = executionProto.modelCode
    if executionProto.HasField('lastLiquidity'): execution.lastLiquidity = executionProto.lastLiquidity
    if executionProto.HasField('isPriceRevisionPending'): execution.pendingPriceRevision = executionProto.isPriceRevisionPending
    if executionProto.HasField('submitter'): execution.submitter = executionProto.submitter
    if executionProto.HasField('optExerciseOrLapseType'): execution.optExerciseOrLapseType = getEnumTypeFromString(OptionExerciseType, executionProto.optExerciseOrLapseType)
    return execution

@staticmethod
def decodeOrder(contractProto: ContractProto, orderProto: OrderProto) -> Order:
    order = Order()
    if orderProto.HasField('action'): order.action = orderProto.action
    if orderProto.HasField('totalQuantity'): order.totalQuantity = orderProto.totalQuantity
    if orderProto.HasField('orderType'): order.orderType = orderProto.orderType
    if orderProto.HasField('lmtPrice'): order.lmtPrice = orderProto.lmtPrice
    if orderProto.HasField('auxPrice'): order.auxPrice = orderProto.auxPrice
    if orderProto.HasField('tif'): order.tif = orderProto.tif
    if orderProto.HasField('ocaGroup'): order.ocaGroup = orderProto.ocaGroup
    if orderProto.HasField('account'): order.account = orderProto.account
    if orderProto.HasField('openClose'): order.openClose = orderProto.openClose
    if orderProto.HasField('origin'): order.origin = orderProto.origin
    if orderProto.HasField('orderRef'): order.orderRef = orderProto.orderRef
    if orderProto.HasField('clientId'): order.clientId = orderProto.clientId
    if orderProto.HasField('permId'): order.permId = orderProto.permId
    if orderProto.HasField('outsideRth'): order.outsideRth = orderProto.outsideRth
    if orderProto.HasField('hidden'): order.hidden = orderProto.hidden
    if orderProto.HasField('discretionaryAmt'): order.discretionaryAmt = orderProto.discretionaryAmt
    if orderProto.HasField('goodAfterTime'): order.goodAfterTime = orderProto.goodAfterTime
    if orderProto.HasField('faGroup'): order.faGroup = orderProto.faGroup
    if orderProto.HasField('faMethod'): order.faMethod = orderProto.faMethod
    if orderProto.HasField('faPercentage'): order.faPercentage = orderProto.faPercentage
    if orderProto.HasField('modelCode'): order.modelCode = orderProto.modelCode
    if orderProto.HasField('goodTillDate'): order.goodTillDate = orderProto.goodTillDate
    if orderProto.HasField('rule80A'): order.rule80A = orderProto.rule80A
    if orderProto.HasField('percentOffset'): order.percentOffset = orderProto.percentOffset
    if orderProto.HasField('settlingFirm'): order.settlingFirm = orderProto.settlingFirm
    if orderProto.HasField('shortSaleSlot'): order.shortSaleSlot = orderProto.shortSaleSlot
    if orderProto.HasField('designatedLocation'): order.designatedLocation = orderProto.designatedLocation
    if orderProto.HasField('exemptCode'): order.exemptCode = orderProto.exemptCode
    if orderProto.HasField('startingPrice'): order.startingPrice = orderProto.startingPrice
    if orderProto.HasField('stockRefPrice'): order.stockRefPrice = orderProto.stockRefPrice
    if orderProto.HasField('delta'): order.delta = orderProto.delta
    if orderProto.HasField('stockRangeLower'): order.stockRangeLower = orderProto.stockRangeLower
    if orderProto.HasField('stockRangeUpper'): order.stockRangeUpper = orderProto.stockRangeUpper
    if orderProto.HasField('displaySize'): order.displaySize = orderProto.displaySize
    if orderProto.HasField('blockOrder'): order.blockOrder = orderProto.blockOrder
    if orderProto.HasField('sweepToFill'): order.sweepToFill = orderProto.sweepToFill
    if orderProto.HasField('allOrNone'): order.allOrNone = orderProto.allOrNone
    if orderProto.HasField('minQty'): order.minQty = orderProto.minQty
    if orderProto.HasField('ocaType'): order.ocaType = orderProto.ocaType
    if orderProto.HasField('parentId'): order.parentId = orderProto.parentId
    if orderProto.HasField('triggerMethod'): order.triggerMethod = orderProto.triggerMethod
    if orderProto.HasField('volatility'): order.volatility = orderProto.volatility
    if orderProto.HasField('volatilityType'): order.volatilityType = orderProto.volatilityType
    if orderProto.HasField('deltaNeutralOrderType'): order.deltaNeutralOrderType = orderProto.deltaNeutralOrderType
    if orderProto.HasField('deltaNeutralAuxPrice'): order.deltaNeutralAuxPrice = orderProto.deltaNeutralAuxPrice
    if orderProto.HasField('deltaNeutralConId'): order.deltaNeutralConId = orderProto.deltaNeutralConId
    if orderProto.HasField('deltaNeutralSettlingFirm'): order.ddeltaNeutralSettlingFirm = orderProto.deltaNeutralSettlingFirm
    if orderProto.HasField('deltaNeutralClearingAccount'): order.deltaNeutralClearingAccount = orderProto.deltaNeutralClearingAccount
    if orderProto.HasField('deltaNeutralClearingIntent'): order.deltaNeutralClearingIntent = orderProto.deltaNeutralClearingIntent
    if orderProto.HasField('deltaNeutralOpenClose'): order.deltaNeutralOpenClose = orderProto.deltaNeutralOpenClose
    if orderProto.HasField('deltaNeutralShortSale'): order.deltaNeutralShortSale = orderProto.deltaNeutralShortSale
    if orderProto.HasField('deltaNeutralShortSaleSlot'): order.deltaNeutralShortSaleSlot = orderProto.deltaNeutralShortSaleSlot
    if orderProto.HasField('deltaNeutralDesignatedLocation'): order.deltaNeutralDesignatedLocation = orderProto.deltaNeutralDesignatedLocation
    if orderProto.HasField('continuousUpdate'): order.continuousUpdate = orderProto.continuousUpdate
    if orderProto.HasField('referencePriceType'): order.referencePriceType = orderProto.referencePriceType
    if orderProto.HasField('trailStopPrice'): order.trailStopPrice = orderProto.trailStopPrice
    if orderProto.HasField('trailingPercent'): order.trailingPercent = orderProto.trailingPercent

    orderComboLegs = decodeOrderComboLegs(contractProto)
    if orderComboLegs is not None and orderComboLegs: order.orderComboLegs = orderComboLegs

    order.smartComboRoutingParams = decodeTagValueList(orderProto.smartComboRoutingParams)

    if orderProto.HasField('scaleInitLevelSize'): order.scaleInitLevelSize = orderProto.scaleInitLevelSize
    if orderProto.HasField('scaleSubsLevelSize'): order.scaleSubsLevelSize = orderProto.scaleSubsLevelSize
    if orderProto.HasField('scalePriceIncrement'): order.scalePriceIncrement = orderProto.scalePriceIncrement
    if orderProto.HasField('scalePriceAdjustValue'): order.scalePriceAdjustValue = orderProto.scalePriceAdjustValue
    if orderProto.HasField('scalePriceAdjustInterval'): order.scalePriceAdjustInterval = orderProto.scalePriceAdjustInterval
    if orderProto.HasField('scaleProfitOffset'): order.scaleProfitOffset = orderProto.scaleProfitOffset
    if orderProto.HasField('scaleAutoReset'): order.scaleAutoReset = orderProto.scaleAutoReset
    if orderProto.HasField('scaleInitPosition'): order.scaleInitPosition = orderProto.scaleInitPosition
    if orderProto.HasField('scaleInitFillQty'): order.scaleInitFillQty = orderProto.scaleInitFillQty
    if orderProto.HasField('scaleRandomPercent'): order.scaleRandomPercent = orderProto.scaleRandomPercent
    if orderProto.HasField('hedgeType'): order.hedgeType = orderProto.hedgeType
    if orderProto.HasField('hedgeType') and orderProto.HasField('hedgeParam') and orderProto.hedgeType: order.hedgeParam = orderProto.hedgeParam
    if orderProto.HasField('optOutSmartRouting'): order.optOutSmartRouting = orderProto.optOutSmartRouting
    if orderProto.HasField('clearingAccount'): order.clearingAccount = orderProto.clearingAccount
    if orderProto.HasField('clearingIntent'): order.clearingIntent = orderProto.clearingIntent
    if orderProto.HasField('notHeld'): order.notHeld = orderProto.notHeld

    if orderProto.HasField('algoStrategy'): 
        order.algoStrategy = orderProto.algoStrategy
        order.algoParams = decodeTagValueList(orderProto.algoParams)

    if orderProto.HasField('solicited'): order.solicited = orderProto.solicited
    if orderProto.HasField('whatIf'): order.whatIf = orderProto.whatIf
    if orderProto.HasField('randomizeSize'): order.randomizeSize = orderProto.randomizeSize
    if orderProto.HasField('randomizePrice'): order.randomizePrice = orderProto.randomizePrice
    if orderProto.HasField('referenceContractId'): order.referenceContractId = orderProto.referenceContractId
    if orderProto.HasField('isPeggedChangeAmountDecrease'): order.isPeggedChangeAmountDecrease = orderProto.isPeggedChangeAmountDecrease
    if orderProto.HasField('peggedChangeAmount'): order.peggedChangeAmount = orderProto.peggedChangeAmount
    if orderProto.HasField('referenceChangeAmount'): order.referenceChangeAmount = orderProto.referenceChangeAmount
    if orderProto.HasField('referenceExchangeId'): order.referenceExchangeId = orderProto.referenceExchangeId

    conditions = decodeConditions(orderProto)
    if conditions is not None and conditions: order.conditions = conditions
    if orderProto.HasField('conditionsIgnoreRth'): order.conditionsIgnoreRth = orderProto.conditionsIgnoreRth
    if orderProto.HasField('conditionsCancelOrder'): order.conditionsCancelOrder = orderProto.conditionsCancelOrder

    if orderProto.HasField('adjustedOrderType'): order.adjustedOrderType = orderProto.adjustedOrderType
    if orderProto.HasField('triggerPrice'): order.triggerPrice = orderProto.triggerPrice
    if orderProto.HasField('lmtPriceOffset'): order.lmtPriceOffset = orderProto.lmtPriceOffset
    if orderProto.HasField('adjustedStopPrice'): order.adjustedStopPrice = orderProto.adjustedStopPrice
    if orderProto.HasField('adjustedStopLimitPrice'): order.adjustedStopLimitPrice = orderProto.adjustedStopLimitPrice
    if orderProto.HasField('adjustedTrailingAmount'): order.adjustedTrailingAmount = orderProto.adjustedTrailingAmount
    if orderProto.HasField('adjustableTrailingUnit'): order.adjustableTrailingUnit = orderProto.adjustableTrailingUnit

    softDollarTier = decodeSoftDollarTier(orderProto)
    if softDollarTier is not None: order.softDollarTier = softDollarTier

    if orderProto.HasField('cashQty'): order.cashQty = orderProto.cashQty
    if orderProto.HasField('dontUseAutoPriceForHedge'): order.dontUseAutoPriceForHedge = orderProto.dontUseAutoPriceForHedge
    if orderProto.HasField('isOmsContainer'): order.isOmsContainer = orderProto.isOmsContainer
    if orderProto.HasField('discretionaryUpToLimitPrice'): order.discretionaryUpToLimitPrice = orderProto.discretionaryUpToLimitPrice
    if orderProto.HasField('usePriceMgmtAlgo'): order.usePriceMgmtAlgo = orderProto.usePriceMgmtAlgo
    if orderProto.HasField('duration'): order.duration = orderProto.duration
    if orderProto.HasField('postToAts'): order.postToAts = orderProto.postToAts
    if orderProto.HasField('autoCancelParent'): order.autoCancelParent = orderProto.autoCancelParent
    if orderProto.HasField('minTradeQty'): order.minTradeQty = orderProto.minTradeQty
    if orderProto.HasField('minCompeteSize'): order.minCompeteSize = orderProto.minCompeteSize
    if orderProto.HasField('competeAgainstBestOffset'): order.competeAgainstBestOffset = orderProto.competeAgainstBestOffset
    if orderProto.HasField('midOffsetAtWhole'): order.midOffsetAtWhole = orderProto.midOffsetAtWhole
    if orderProto.HasField('midOffsetAtHalf'): order.midOffsetAtHalf = orderProto.midOffsetAtHalf
    if orderProto.HasField('customerAccount'): order.customerAccount = orderProto.customerAccount
    if orderProto.HasField('professionalCustomer'): order.professionalCustomer = orderProto.professionalCustomer
    if orderProto.HasField('bondAccruedInterest'): order.bondAccruedInterest = orderProto.bondAccruedInterest
    if orderProto.HasField('includeOvernight'): order.includeOvernight = orderProto.includeOvernight
    if orderProto.HasField('extOperator'): order.extOperator = orderProto.extOperator
    if orderProto.HasField('manualOrderIndicator'): order.manualOrderIndicator = orderProto.manualOrderIndicator
    if orderProto.HasField('submitter'): order.submitter = orderProto.submitter
    if orderProto.HasField('imbalanceOnly'): order.imbalanceOnly = orderProto.imbalanceOnly

    return order

def decodeConditions(orderProto: OrderProto) -> list[OrderCondition]:
    orderConditions = []
    orderConditionsProtoList = []
    if orderProto.conditions is not None: orderConditionsProtoList = orderProto.conditions

    if orderConditionsProtoList:
        for orderConditionProto in orderConditionsProtoList:
            conditionType = orderConditionProto.type if orderConditionProto.HasField('type') else 0

            if OrderCondition.Price == conditionType:
                condition = createPriceCondition(orderConditionProto)
            elif OrderCondition.Time == conditionType:
                condition = createTimeCondition(orderConditionProto)
            elif OrderCondition.Margin == conditionType:
                condition = createMarginCondition(orderConditionProto)
            elif OrderCondition.Execution == conditionType:
                condition = createExecutionCondition(orderConditionProto)
            elif OrderCondition.Volume == conditionType:
                condition = createVolumeCondition(orderConditionProto)
            elif OrderCondition.PercentChange == conditionType:
                condition = createPercentChangeCondition(orderConditionProto)

            if condition is not None: orderConditions.append(condition)

    return orderConditions

@staticmethod
def setConditionFields(orderConditionProto: OrderConditionProto, orderCondition: OrderCondition):
    if orderConditionProto.HasField('isConjunctionConnection'): orderCondition.isConjunctionConnection = orderConditionProto.isConjunctionConnection

@staticmethod
def setOperatorConditionFields(orderConditionProto: OrderConditionProto, operatorCondition: OperatorCondition):
    setConditionFields(orderConditionProto, operatorCondition)
    if orderConditionProto.HasField('isMore'): operatorCondition.isMore = orderConditionProto.isMore

@staticmethod
def setContractConditionFields(orderConditionProto: OrderConditionProto, contractCondition: ContractCondition):
    setOperatorConditionFields(orderConditionProto, contractCondition)
    if orderConditionProto.HasField('conId'): contractCondition.conId = orderConditionProto.conId
    if orderConditionProto.HasField('exchange'): contractCondition.exchange = orderConditionProto.exchange

@staticmethod
def createPriceCondition(orderConditionProto: OrderConditionProto) -> PriceCondition:
    priceCondition = PriceCondition()
    setContractConditionFields(orderConditionProto, priceCondition)
    if orderConditionProto.HasField('price'): priceCondition.price = orderConditionProto.price
    if orderConditionProto.HasField('triggerMethod'): priceCondition.triggerMethod = orderConditionProto.triggerMethod
    return priceCondition

@staticmethod
def createTimeCondition(orderConditionProto: OrderConditionProto) -> TimeCondition:
    timeCondition = TimeCondition()
    setOperatorConditionFields(orderConditionProto, timeCondition)
    if orderConditionProto.HasField('time'): timeCondition.time = orderConditionProto.time
    return timeCondition

@staticmethod
def createMarginCondition(orderConditionProto: OrderConditionProto) -> MarginCondition:
    marginCondition = MarginCondition()
    setOperatorConditionFields(orderConditionProto, marginCondition)
    if orderConditionProto.HasField('percent'): marginCondition.percent = orderConditionProto.percent
    return marginCondition

@staticmethod
def createExecutionCondition(orderConditionProto: OrderConditionProto) -> ExecutionCondition:
    executionCondition = ExecutionCondition()
    setConditionFields(orderConditionProto, executionCondition)
    if orderConditionProto.HasField('secType'): executionCondition.secType = orderConditionProto.secType
    if orderConditionProto.HasField('exchange'): executionCondition.exchange = orderConditionProto.exchange
    if orderConditionProto.HasField('symbol'): executionCondition.symbol = orderConditionProto.symbol
    return executionCondition

@staticmethod
def createVolumeCondition(orderConditionProto: OrderConditionProto) -> VolumeCondition:
    volumeCondition = VolumeCondition()
    setContractConditionFields(orderConditionProto, volumeCondition)
    if orderConditionProto.HasField('volume'): volumeCondition.volume = orderConditionProto.volume
    return volumeCondition

@staticmethod
def createPercentChangeCondition(orderConditionProto: OrderConditionProto) -> PercentChangeCondition:
    percentChangeCondition = PercentChangeCondition()
    setContractConditionFields(orderConditionProto, percentChangeCondition)
    if orderConditionProto.HasField('changePercent'): percentChangeCondition.changePercent = orderConditionProto.changePercent
    return percentChangeCondition

@staticmethod
def decodeSoftDollarTier(orderProto: OrderProto) -> SoftDollarTier:
    name = ""
    value = ""
    displayName = ""
    softDollarTierProto = SoftDollarTierProto()
    if orderProto.softDollarTier is not None: softDollarTierProto = orderProto.softDollarTier
    if softDollarTierProto.HasField('name'): name = softDollarTierProto.name
    if softDollarTierProto.HasField('value'): value = softDollarTierProto.value
    if softDollarTierProto.HasField('displayName'): displayName = softDollarTierProto.displayName
    softDollarTier = SoftDollarTier(name, value, displayName)

    return softDollarTier

@staticmethod
def decodeTagValueList(protoMap: dict[str, str]) -> list[TagValue]:
    tagValueList = []
    if protoMap is not None and protoMap:
        for tag, value in protoMap.items():
            tagValue = TagValue()
            tagValue.tag = tag
            tagValue.value = value
            tagValueList.append(tagValue)
    return tagValueList

@staticmethod
def decodeOrderState(orderStateProto: OrderStateProto) -> OrderState:
    orderState = OrderState()
    if orderStateProto.HasField('status'): orderState.status = orderStateProto.status
    if orderStateProto.HasField('initMarginBefore'): orderState.initMarginBefore = orderStateProto.initMarginBefore
    if orderStateProto.HasField('maintMarginBefore'): orderState.maintMarginBefore = decimalMaxString(orderStateProto.maintMarginBefore)
    if orderStateProto.HasField('equityWithLoanBefore'): orderState.equityWithLoanBefore = decimalMaxString(orderStateProto.equityWithLoanBefore)
    if orderStateProto.HasField('initMarginChange'): orderState.initMarginChange = decimalMaxString(orderStateProto.initMarginChange)
    if orderStateProto.HasField('maintMarginChange'): orderState.maintMarginChange = decimalMaxString(orderStateProto.maintMarginChange)
    if orderStateProto.HasField('equityWithLoanChange'): orderState.equityWithLoanChange = decimalMaxString(orderStateProto.equityWithLoanChange)
    if orderStateProto.HasField('initMarginAfter'): orderState.initMarginAfter = decimalMaxString(orderStateProto.initMarginAfter)
    if orderStateProto.HasField('maintMarginAfter'): orderState.maintMarginAfter = decimalMaxString(orderStateProto.maintMarginAfter)
    if orderStateProto.HasField('equityWithLoanAfter'): orderState.equityWithLoanAfter = decimalMaxString(orderStateProto.equityWithLoanAfter)
    if orderStateProto.HasField('commissionAndFees'): orderState.commissionAndFees = orderStateProto.commissionAndFees
    if orderStateProto.HasField('minCommissionAndFees'): orderState.minCommissionAndFees = orderStateProto.minCommissionAndFees
    if orderStateProto.HasField('maxCommissionAndFees'): orderState.maxCommissionAndFees = orderStateProto.maxCommissionAndFees
    if orderStateProto.HasField('commissionAndFeesCurrency'): orderState.commissionAndFeesCurrency = orderStateProto.commissionAndFeesCurrency
    if orderStateProto.HasField('warningText'): orderState.warningText = orderStateProto.warningText
    if orderStateProto.HasField('marginCurrency'): orderState.marginCurrency = orderStateProto.marginCurrency
    if orderStateProto.HasField('initMarginBeforeOutsideRTH'): orderState.initMarginBeforeOutsideRTH = orderStateProto.initMarginBeforeOutsideRTH
    if orderStateProto.HasField('maintMarginBeforeOutsideRTH'): orderState.maintMarginBeforeOutsideRTH = orderStateProto.maintMarginBeforeOutsideRTH
    if orderStateProto.HasField('equityWithLoanBeforeOutsideRTH'): orderState.equityWithLoanBeforeOutsideRTH = orderStateProto.equityWithLoanBeforeOutsideRTH
    if orderStateProto.HasField('initMarginChangeOutsideRTH'): orderState.initMarginChangeOutsideRTH = orderStateProto.initMarginChangeOutsideRTH
    if orderStateProto.HasField('maintMarginChangeOutsideRTH'): orderState.maintMarginChangeOutsideRTH = orderStateProto.maintMarginChangeOutsideRTH
    if orderStateProto.HasField('equityWithLoanChangeOutsideRTH'): orderState.equityWithLoanChangeOutsideRTH = orderStateProto.equityWithLoanChangeOutsideRTH
    if orderStateProto.HasField('initMarginAfterOutsideRTH'): orderState.initMarginAfterOutsideRTH = orderStateProto.initMarginAfterOutsideRTH
    if orderStateProto.HasField('maintMarginAfterOutsideRTH'): orderState.maintMarginAfterOutsideRTH = orderStateProto.maintMarginAfterOutsideRTH
    if orderStateProto.HasField('equityWithLoanAfterOutsideRTH'): orderState.equityWithLoanAfterOutsideRTH = orderStateProto.equityWithLoanAfterOutsideRTH
    if orderStateProto.HasField('suggestedSize'): orderState.suggestedSize = Decimal(orderStateProto.suggestedSize)
    if orderStateProto.HasField('rejectReason'): orderState.rejectReason = orderStateProto.rejectReason

    orderAllocations = decodeOrderAllocations(orderStateProto)
    if orderAllocations is not None and orderAllocations: orderState.orderAllocations = orderAllocations

    return orderState

@staticmethod
def decodeOrderAllocations(orderStateProto: OrderStateProto) -> list[OrderAllocation]:
    orderAllocations = []
    orderAllocationProtoList = []
    if orderStateProto.orderAllocations is not None: orderAllocationProtoList = orderStateProto.orderAllocations
    if orderAllocationProtoList:
        for orderAllocationProto in orderAllocationProtoList:
            orderAllocation = OrderAllocation()
            if orderAllocationProto.HasField('account'): orderAllocation.account = orderAllocationProto.account
            if orderAllocationProto.HasField('position'): orderAllocation.position = Decimal(orderAllocationProto.position)
            if orderAllocationProto.HasField('positionDesired'): orderAllocation.positionDesired = Decimal(orderAllocationProto.positionDesired)
            if orderAllocationProto.HasField('positionAfter'): orderAllocation.positionAfter = Decimal(orderAllocationProto.positionAfter)
            if orderAllocationProto.HasField('desiredAllocQty'): orderAllocation.desiredAllocQty = Decimal(orderAllocationProto.desiredAllocQty)
            if orderAllocationProto.HasField('allowedAllocQty'): orderAllocation.allowedAllocQty = Decimal(orderAllocationProto.allowedAllocQty)
            if orderAllocationProto.HasField('isMonetary'): orderAllocation.isMonetary = orderAllocationProto.isMonetary
            orderAllocations.append(orderAllocation)
    return orderAllocations
