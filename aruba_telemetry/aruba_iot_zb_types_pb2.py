# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruba-iot-zb-types.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import aruba_iot_types_pb2 as aruba__iot__types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x61ruba-iot-zb-types.proto\x12\x0f\x61ruba_telemetry\x1a\x15\x61ruba-iot-types.proto\"A\n\x05ZbEPC\x12\x10\n\x08\x65ndpoint\x18\x01 \x01(\r\x12\x12\n\nprofile_id\x18\x02 \x01(\r\x12\x12\n\ncluster_id\x18\x03 \x01(\r\"N\n\x06ZbE2PC\x12+\n\x0b\x64\x65stination\x18\x01 \x01(\x0b\x32\x16.aruba_telemetry.ZbEPC\x12\x17\n\x0fsource_endpoint\x18\x02 \x01(\r*%\n\x08ZbResult\x12\r\n\tSUCCEEDED\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01*\x13\n\tZbAckCode\x12\x06\n\x02OK\x10\x00')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruba_iot_zb_types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ZBRESULT']._serialized_start=215
  _globals['_ZBRESULT']._serialized_end=252
  _globals['_ZBACKCODE']._serialized_start=254
  _globals['_ZBACKCODE']._serialized_end=273
  _globals['_ZBEPC']._serialized_start=68
  _globals['_ZBEPC']._serialized_end=133
  _globals['_ZBE2PC']._serialized_start=135
  _globals['_ZBE2PC']._serialized_end=213
# @@protoc_insertion_point(module_scope)