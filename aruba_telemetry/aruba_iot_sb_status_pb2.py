# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruba-iot-sb-status.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x61ruba-iot-sb-status.proto\x12\x0f\x61ruba_telemetry\"^\n\rConnectStatus\x12\x31\n\x0b\x63onnectCode\x18\x01 \x01(\x0e\x32\x1c.aruba_telemetry.ConnectCode\x12\x1a\n\x12\x63onnectDescription\x18\x02 \x01(\t*,\n\x0b\x43onnectCode\x12\x0c\n\x08statusOK\x10\x00\x12\x0f\n\x0btokenExpire\x10\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruba_iot_sb_status_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CONNECTCODE']._serialized_start=142
  _globals['_CONNECTCODE']._serialized_end=186
  _globals['_CONNECTSTATUS']._serialized_start=46
  _globals['_CONNECTSTATUS']._serialized_end=140
# @@protoc_insertion_point(module_scope)
