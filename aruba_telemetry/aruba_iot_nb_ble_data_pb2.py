# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruba-iot-nb-ble-data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='aruba-iot-nb-ble-data.proto',
  package='aruba_telemetry',
  serialized_pb=_b('\n\x1b\x61ruba-iot-nb-ble-data.proto\x12\x0f\x61ruba_telemetry\"d\n\x07\x42leData\x12\x0b\n\x03mac\x18\x01 \x01(\x0c\x12\x30\n\tframeType\x18\x02 \x01(\x0e\x32\x1d.aruba_telemetry.BleFrameType\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x12\x0c\n\x04rssi\x18\x04 \x01(\x11*d\n\x0c\x42leFrameType\x12\x0b\n\x07\x61\x64v_ind\x10\x00\x12\x12\n\x0e\x61\x64v_direct_ind\x10\x01\x12\x13\n\x0f\x61\x64v_nonconn_ind\x10\x02\x12\x0c\n\x08scan_rsp\x10\x04\x12\x10\n\x0c\x61\x64v_scan_ind\x10\x06')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_BLEFRAMETYPE = _descriptor.EnumDescriptor(
  name='BleFrameType',
  full_name='aruba_telemetry.BleFrameType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='adv_ind', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='adv_direct_ind', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='adv_nonconn_ind', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='scan_rsp', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='adv_scan_ind', index=4, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=150,
  serialized_end=250,
)
_sym_db.RegisterEnumDescriptor(_BLEFRAMETYPE)

BleFrameType = enum_type_wrapper.EnumTypeWrapper(_BLEFRAMETYPE)
adv_ind = 0
adv_direct_ind = 1
adv_nonconn_ind = 2
scan_rsp = 4
adv_scan_ind = 6



_BLEDATA = _descriptor.Descriptor(
  name='BleData',
  full_name='aruba_telemetry.BleData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mac', full_name='aruba_telemetry.BleData.mac', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='frameType', full_name='aruba_telemetry.BleData.frameType', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='aruba_telemetry.BleData.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rssi', full_name='aruba_telemetry.BleData.rssi', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=148,
)

_BLEDATA.fields_by_name['frameType'].enum_type = _BLEFRAMETYPE
DESCRIPTOR.message_types_by_name['BleData'] = _BLEDATA
DESCRIPTOR.enum_types_by_name['BleFrameType'] = _BLEFRAMETYPE

BleData = _reflection.GeneratedProtocolMessageType('BleData', (_message.Message,), dict(
  DESCRIPTOR = _BLEDATA,
  __module__ = 'aruba_iot_nb_ble_data_pb2'
  # @@protoc_insertion_point(class_scope:aruba_telemetry.BleData)
  ))
_sym_db.RegisterMessage(BleData)


# @@protoc_insertion_point(module_scope)