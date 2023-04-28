# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: orders.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from TinkoffPy.grpc import common_pb2 as common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0corders.proto\x12%tinkoff.public.invest.api.contract.v1\x1a\x0c\x63ommon.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\'\n\x13TradesStreamRequest\x12\x10\n\x08\x61\x63\x63ounts\x18\x01 \x03(\t\"\xaa\x01\n\x14TradesStreamResponse\x12J\n\x0corder_trades\x18\x01 \x01(\x0b\x32\x32.tinkoff.public.invest.api.contract.v1.OrderTradesH\x00\x12;\n\x04ping\x18\x02 \x01(\x0b\x32+.tinkoff.public.invest.api.contract.v1.PingH\x00\x42\t\n\x07payload\"\x96\x02\n\x0bOrderTrades\x12\x10\n\x08order_id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12H\n\tdirection\x18\x03 \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.OrderDirection\x12\x0c\n\x04\x66igi\x18\x04 \x01(\t\x12\x41\n\x06trades\x18\x05 \x03(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.OrderTrade\x12\x12\n\naccount_id\x18\x06 \x01(\t\x12\x16\n\x0einstrument_uid\x18\x07 \x01(\t\"\xa0\x01\n\nOrderTrade\x12-\n\tdate_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12?\n\x05price\x18\x02 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x10\n\x08quantity\x18\x03 \x01(\x03\x12\x10\n\x08trade_id\x18\x04 \x01(\t\"\xc0\x02\n\x10PostOrderRequest\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\x03\x12?\n\x05price\x18\x03 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12H\n\tdirection\x18\x04 \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.OrderDirection\x12\x12\n\naccount_id\x18\x05 \x01(\t\x12\x44\n\norder_type\x18\x06 \x01(\x0e\x32\x30.tinkoff.public.invest.api.contract.v1.OrderType\x12\x10\n\x08order_id\x18\x07 \x01(\t\x12\x15\n\rinstrument_id\x18\x08 \x01(\t\"\xf9\x07\n\x11PostOrderResponse\x12\x10\n\x08order_id\x18\x01 \x01(\t\x12\x62\n\x17\x65xecution_report_status\x18\x02 \x01(\x0e\x32\x41.tinkoff.public.invest.api.contract.v1.OrderExecutionReportStatus\x12\x16\n\x0elots_requested\x18\x03 \x01(\x03\x12\x15\n\rlots_executed\x18\x04 \x01(\x03\x12N\n\x13initial_order_price\x18\x05 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12O\n\x14\x65xecuted_order_price\x18\x06 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12M\n\x12total_order_amount\x18\x07 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12M\n\x12initial_commission\x18\x08 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12N\n\x13\x65xecuted_commission\x18\t \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x44\n\taci_value\x18\n \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x0c\n\x04\x66igi\x18\x0b \x01(\t\x12H\n\tdirection\x18\x0c \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.OrderDirection\x12Q\n\x16initial_security_price\x18\r \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x44\n\norder_type\x18\x0e \x01(\x0e\x32\x30.tinkoff.public.invest.api.contract.v1.OrderType\x12\x0f\n\x07message\x18\x0f \x01(\t\x12P\n\x16initial_order_price_pt\x18\x10 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x16\n\x0einstrument_uid\x18\x11 \x01(\t\":\n\x12\x43\x61ncelOrderRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x10\n\x08order_id\x18\x02 \x01(\t\"?\n\x13\x43\x61ncelOrderResponse\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"<\n\x14GetOrderStateRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x10\n\x08order_id\x18\x02 \x01(\t\"&\n\x10GetOrdersRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\"V\n\x11GetOrdersResponse\x12\x41\n\x06orders\x18\x01 \x03(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.OrderState\"\xf0\x08\n\nOrderState\x12\x10\n\x08order_id\x18\x01 \x01(\t\x12\x62\n\x17\x65xecution_report_status\x18\x02 \x01(\x0e\x32\x41.tinkoff.public.invest.api.contract.v1.OrderExecutionReportStatus\x12\x16\n\x0elots_requested\x18\x03 \x01(\x03\x12\x15\n\rlots_executed\x18\x04 \x01(\x03\x12N\n\x13initial_order_price\x18\x05 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12O\n\x14\x65xecuted_order_price\x18\x06 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12M\n\x12total_order_amount\x18\x07 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12Q\n\x16\x61verage_position_price\x18\x08 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12M\n\x12initial_commission\x18\t \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12N\n\x13\x65xecuted_commission\x18\n \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x0c\n\x04\x66igi\x18\x0b \x01(\t\x12H\n\tdirection\x18\x0c \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.OrderDirection\x12Q\n\x16initial_security_price\x18\r \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x41\n\x06stages\x18\x0e \x03(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.OrderStage\x12M\n\x12service_commission\x18\x0f \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x10\n\x08\x63urrency\x18\x10 \x01(\t\x12\x44\n\norder_type\x18\x11 \x01(\x0e\x32\x30.tinkoff.public.invest.api.contract.v1.OrderType\x12.\n\norder_date\x18\x12 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x0einstrument_uid\x18\x13 \x01(\t\"r\n\nOrderStage\x12@\n\x05price\x18\x01 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x10\n\x08quantity\x18\x02 \x01(\x03\x12\x10\n\x08trade_id\x18\x03 \x01(\t\"\xed\x01\n\x13ReplaceOrderRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x10\n\x08order_id\x18\x06 \x01(\t\x12\x17\n\x0fidempotency_key\x18\x07 \x01(\t\x12\x10\n\x08quantity\x18\x0b \x01(\x03\x12?\n\x05price\x18\x0c \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x44\n\nprice_type\x18\r \x01(\x0e\x32\x30.tinkoff.public.invest.api.contract.v1.PriceType*d\n\x0eOrderDirection\x12\x1f\n\x1bORDER_DIRECTION_UNSPECIFIED\x10\x00\x12\x17\n\x13ORDER_DIRECTION_BUY\x10\x01\x12\x18\n\x14ORDER_DIRECTION_SELL\x10\x02*T\n\tOrderType\x12\x1a\n\x16ORDER_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10ORDER_TYPE_LIMIT\x10\x01\x12\x15\n\x11ORDER_TYPE_MARKET\x10\x02*\x80\x02\n\x1aOrderExecutionReportStatus\x12\'\n#EXECUTION_REPORT_STATUS_UNSPECIFIED\x10\x00\x12 \n\x1c\x45XECUTION_REPORT_STATUS_FILL\x10\x01\x12$\n EXECUTION_REPORT_STATUS_REJECTED\x10\x02\x12%\n!EXECUTION_REPORT_STATUS_CANCELLED\x10\x03\x12\x1f\n\x1b\x45XECUTION_REPORT_STATUS_NEW\x10\x04\x12)\n%EXECUTION_REPORT_STATUS_PARTIALLYFILL\x10\x05*V\n\tPriceType\x12\x1a\n\x16PRICE_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10PRICE_TYPE_POINT\x10\x01\x12\x17\n\x13PRICE_TYPE_CURRENCY\x10\x02\x32\xa1\x01\n\x13OrdersStreamService\x12\x89\x01\n\x0cTradesStream\x12:.tinkoff.public.invest.api.contract.v1.TradesStreamRequest\x1a;.tinkoff.public.invest.api.contract.v1.TradesStreamResponse0\x01\x32\x9e\x05\n\rOrdersService\x12~\n\tPostOrder\x12\x37.tinkoff.public.invest.api.contract.v1.PostOrderRequest\x1a\x38.tinkoff.public.invest.api.contract.v1.PostOrderResponse\x12\x84\x01\n\x0b\x43\x61ncelOrder\x12\x39.tinkoff.public.invest.api.contract.v1.CancelOrderRequest\x1a:.tinkoff.public.invest.api.contract.v1.CancelOrderResponse\x12\x7f\n\rGetOrderState\x12;.tinkoff.public.invest.api.contract.v1.GetOrderStateRequest\x1a\x31.tinkoff.public.invest.api.contract.v1.OrderState\x12~\n\tGetOrders\x12\x37.tinkoff.public.invest.api.contract.v1.GetOrdersRequest\x1a\x38.tinkoff.public.invest.api.contract.v1.GetOrdersResponse\x12\x84\x01\n\x0cReplaceOrder\x12:.tinkoff.public.invest.api.contract.v1.ReplaceOrderRequest\x1a\x38.tinkoff.public.invest.api.contract.v1.PostOrderResponseBa\n\x1cru.tinkoff.piapi.contract.v1P\x01Z\x0c./;investapi\xa2\x02\x05TIAPI\xaa\x02\x14Tinkoff.InvestApi.V1\xca\x02\x11Tinkoff\\Invest\\V1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'orders_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034ru.tinkoff.piapi.contract.v1P\001Z\014./;investapi\242\002\005TIAPI\252\002\024Tinkoff.InvestApi.V1\312\002\021Tinkoff\\Invest\\V1'
  _ORDERDIRECTION._serialized_start=3913
  _ORDERDIRECTION._serialized_end=4013
  _ORDERTYPE._serialized_start=4015
  _ORDERTYPE._serialized_end=4099
  _ORDEREXECUTIONREPORTSTATUS._serialized_start=4102
  _ORDEREXECUTIONREPORTSTATUS._serialized_end=4358
  _PRICETYPE._serialized_start=4360
  _PRICETYPE._serialized_end=4446
  _TRADESSTREAMREQUEST._serialized_start=102
  _TRADESSTREAMREQUEST._serialized_end=141
  _TRADESSTREAMRESPONSE._serialized_start=144
  _TRADESSTREAMRESPONSE._serialized_end=314
  _ORDERTRADES._serialized_start=317
  _ORDERTRADES._serialized_end=595
  _ORDERTRADE._serialized_start=598
  _ORDERTRADE._serialized_end=758
  _POSTORDERREQUEST._serialized_start=761
  _POSTORDERREQUEST._serialized_end=1081
  _POSTORDERRESPONSE._serialized_start=1084
  _POSTORDERRESPONSE._serialized_end=2101
  _CANCELORDERREQUEST._serialized_start=2103
  _CANCELORDERREQUEST._serialized_end=2161
  _CANCELORDERRESPONSE._serialized_start=2163
  _CANCELORDERRESPONSE._serialized_end=2226
  _GETORDERSTATEREQUEST._serialized_start=2228
  _GETORDERSTATEREQUEST._serialized_end=2288
  _GETORDERSREQUEST._serialized_start=2290
  _GETORDERSREQUEST._serialized_end=2328
  _GETORDERSRESPONSE._serialized_start=2330
  _GETORDERSRESPONSE._serialized_end=2416
  _ORDERSTATE._serialized_start=2419
  _ORDERSTATE._serialized_end=3555
  _ORDERSTAGE._serialized_start=3557
  _ORDERSTAGE._serialized_end=3671
  _REPLACEORDERREQUEST._serialized_start=3674
  _REPLACEORDERREQUEST._serialized_end=3911
  _ORDERSSTREAMSERVICE._serialized_start=4449
  _ORDERSSTREAMSERVICE._serialized_end=4610
  _ORDERSSERVICE._serialized_start=4613
  _ORDERSSERVICE._serialized_end=5283
# @@protoc_insertion_point(module_scope)
