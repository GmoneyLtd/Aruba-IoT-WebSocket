# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruba-iot-nb-ble-data.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x61ruba-iot-nb-ble-data.proto\x12\x0f\x61ruba_telemetry\"\xa4\x01\n\x07\x42leData\x12\x0b\n\x03mac\x18\x01 \x01(\x0c\x12\x30\n\tframeType\x18\x02 \x01(\x0e\x32\x1d.aruba_telemetry.BleFrameType\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x12\x0c\n\x04rssi\x18\x04 \x01(\x11\x12.\n\x08\x61\x64\x64rType\x18\x05 \x01(\x0e\x32\x1c.aruba_telemetry.MacAddrType\x12\x0e\n\x06\x61pbMac\x18\x06 \x01(\x0c*d\n\x0c\x42leFrameType\x12\x0b\n\x07\x61\x64v_ind\x10\x00\x12\x12\n\x0e\x61\x64v_direct_ind\x10\x01\x12\x13\n\x0f\x61\x64v_nonconn_ind\x10\x02\x12\x0c\n\x08scan_rsp\x10\x04\x12\x10\n\x0c\x61\x64v_scan_ind\x10\x06*\x81\x01\n\x0bMacAddrType\x12\x14\n\x10\x61\x64\x64r_type_public\x10\x00\x12\x14\n\x10\x61\x64\x64r_type_static\x10\x01\x12$\n addr_type_private_non_resolvable\x10\x02\x12 \n\x1c\x61\x64\x64r_type_private_resolvable\x10\x03')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruba_iot_nb_ble_data_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_BLEFRAMETYPE']._serialized_start=215
  _globals['_BLEFRAMETYPE']._serialized_end=315
  _globals['_MACADDRTYPE']._serialized_start=318
  _globals['_MACADDRTYPE']._serialized_end=447
  _globals['_BLEDATA']._serialized_start=49
  _globals['_BLEDATA']._serialized_end=213
# @@protoc_insertion_point(module_scope)
