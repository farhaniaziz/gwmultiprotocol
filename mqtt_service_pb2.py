# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mqtt_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12mqtt_service.proto\"\'\n\x08mqtt_msg\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\"\x07\n\x05\x45mpty2$\n\x04mqtt\x12\x1c\n\x07publish\x12\t.mqtt_msg\x1a\x06.Emptyb\x06proto3')



_MQTT_MSG = DESCRIPTOR.message_types_by_name['mqtt_msg']
_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
mqtt_msg = _reflection.GeneratedProtocolMessageType('mqtt_msg', (_message.Message,), {
  'DESCRIPTOR' : _MQTT_MSG,
  '__module__' : 'mqtt_service_pb2'
  # @@protoc_insertion_point(class_scope:mqtt_msg)
  })
_sym_db.RegisterMessage(mqtt_msg)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'mqtt_service_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

_MQTT = DESCRIPTOR.services_by_name['mqtt']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MQTT_MSG._serialized_start=22
  _MQTT_MSG._serialized_end=61
  _EMPTY._serialized_start=63
  _EMPTY._serialized_end=70
  _MQTT._serialized_start=72
  _MQTT._serialized_end=108
# @@protoc_insertion_point(module_scope)