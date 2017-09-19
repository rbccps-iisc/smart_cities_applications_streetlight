# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: actuated.proto

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
  name='actuated.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0e\x61\x63tuated.proto\"2\n\x16targetPowerStateParams\x12\x18\n\x10targetPowerState\x18\x01 \x02(\x08\"9\n\x13targetControlPolicy\x12\"\n\rcontrolPolicy\x18\x01 \x02(\x0e\x32\x0b.ctrlPolicy\":\n\x19targetManualControlParams\x12\x1d\n\x15targetBrightnessLevel\x18\x01 \x01(\r\"D\n\x15targetAutoTimerParams\x12\x14\n\x0ctargetOnTime\x18\x01 \x01(\r\x12\x15\n\rtargetOffTime\x18\x02 \x01(\r\"@\n\x13targetAutoLuxParams\x12\x13\n\x0btargetOnLux\x18\x01 \x01(\r\x12\x14\n\x0ctargetOffLux\x18\x02 \x01(\r\"\x87\x02\n\x14targetConfigurations\x12+\n\nPowerState\x18\x01 \x01(\x0b\x32\x17.targetPowerStateParams\x12+\n\rControlPolicy\x18\x02 \x01(\x0b\x32\x14.targetControlPolicy\x12/\n\x0f\x41utoTimerParams\x18\x03 \x01(\x0b\x32\x16.targetAutoTimerParams\x12+\n\rAutoLuxParams\x18\x04 \x01(\x0b\x32\x14.targetAutoLuxParams\x12\x37\n\x13ManualControlParams\x18\x05 \x01(\x0b\x32\x1a.targetManualControlParams*6\n\nctrlPolicy\x12\x0c\n\x08\x41UTO_LUX\x10\x00\x12\x0e\n\nAUTO_TIMER\x10\x01\x12\n\n\x06MANUAL\x10\x02')
)

_CTRLPOLICY = _descriptor.EnumDescriptor(
  name='ctrlPolicy',
  full_name='ctrlPolicy',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AUTO_LUX', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTO_TIMER', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MANUAL', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=591,
  serialized_end=645,
)
_sym_db.RegisterEnumDescriptor(_CTRLPOLICY)

ctrlPolicy = enum_type_wrapper.EnumTypeWrapper(_CTRLPOLICY)
AUTO_LUX = 0
AUTO_TIMER = 1
MANUAL = 2



_TARGETPOWERSTATEPARAMS = _descriptor.Descriptor(
  name='targetPowerStateParams',
  full_name='targetPowerStateParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='targetPowerState', full_name='targetPowerStateParams.targetPowerState', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=68,
)


_TARGETCONTROLPOLICY = _descriptor.Descriptor(
  name='targetControlPolicy',
  full_name='targetControlPolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='controlPolicy', full_name='targetControlPolicy.controlPolicy', index=0,
      number=1, type=14, cpp_type=8, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=127,
)


_TARGETMANUALCONTROLPARAMS = _descriptor.Descriptor(
  name='targetManualControlParams',
  full_name='targetManualControlParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='targetBrightnessLevel', full_name='targetManualControlParams.targetBrightnessLevel', index=0,
      number=1, type=13, cpp_type=3, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=187,
)


_TARGETAUTOTIMERPARAMS = _descriptor.Descriptor(
  name='targetAutoTimerParams',
  full_name='targetAutoTimerParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='targetOnTime', full_name='targetAutoTimerParams.targetOnTime', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='targetOffTime', full_name='targetAutoTimerParams.targetOffTime', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=189,
  serialized_end=257,
)


_TARGETAUTOLUXPARAMS = _descriptor.Descriptor(
  name='targetAutoLuxParams',
  full_name='targetAutoLuxParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='targetOnLux', full_name='targetAutoLuxParams.targetOnLux', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='targetOffLux', full_name='targetAutoLuxParams.targetOffLux', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=259,
  serialized_end=323,
)


_TARGETCONFIGURATIONS = _descriptor.Descriptor(
  name='targetConfigurations',
  full_name='targetConfigurations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='PowerState', full_name='targetConfigurations.PowerState', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ControlPolicy', full_name='targetConfigurations.ControlPolicy', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AutoTimerParams', full_name='targetConfigurations.AutoTimerParams', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AutoLuxParams', full_name='targetConfigurations.AutoLuxParams', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ManualControlParams', full_name='targetConfigurations.ManualControlParams', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=326,
  serialized_end=589,
)

_TARGETCONTROLPOLICY.fields_by_name['controlPolicy'].enum_type = _CTRLPOLICY
_TARGETCONFIGURATIONS.fields_by_name['PowerState'].message_type = _TARGETPOWERSTATEPARAMS
_TARGETCONFIGURATIONS.fields_by_name['ControlPolicy'].message_type = _TARGETCONTROLPOLICY
_TARGETCONFIGURATIONS.fields_by_name['AutoTimerParams'].message_type = _TARGETAUTOTIMERPARAMS
_TARGETCONFIGURATIONS.fields_by_name['AutoLuxParams'].message_type = _TARGETAUTOLUXPARAMS
_TARGETCONFIGURATIONS.fields_by_name['ManualControlParams'].message_type = _TARGETMANUALCONTROLPARAMS
DESCRIPTOR.message_types_by_name['targetPowerStateParams'] = _TARGETPOWERSTATEPARAMS
DESCRIPTOR.message_types_by_name['targetControlPolicy'] = _TARGETCONTROLPOLICY
DESCRIPTOR.message_types_by_name['targetManualControlParams'] = _TARGETMANUALCONTROLPARAMS
DESCRIPTOR.message_types_by_name['targetAutoTimerParams'] = _TARGETAUTOTIMERPARAMS
DESCRIPTOR.message_types_by_name['targetAutoLuxParams'] = _TARGETAUTOLUXPARAMS
DESCRIPTOR.message_types_by_name['targetConfigurations'] = _TARGETCONFIGURATIONS
DESCRIPTOR.enum_types_by_name['ctrlPolicy'] = _CTRLPOLICY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

targetPowerStateParams = _reflection.GeneratedProtocolMessageType('targetPowerStateParams', (_message.Message,), dict(
  DESCRIPTOR = _TARGETPOWERSTATEPARAMS,
  __module__ = 'actuated_pb2'
  # @@protoc_insertion_point(class_scope:targetPowerStateParams)
  ))
_sym_db.RegisterMessage(targetPowerStateParams)

targetControlPolicy = _reflection.GeneratedProtocolMessageType('targetControlPolicy', (_message.Message,), dict(
  DESCRIPTOR = _TARGETCONTROLPOLICY,
  __module__ = 'actuated_pb2'
  # @@protoc_insertion_point(class_scope:targetControlPolicy)
  ))
_sym_db.RegisterMessage(targetControlPolicy)

targetManualControlParams = _reflection.GeneratedProtocolMessageType('targetManualControlParams', (_message.Message,), dict(
  DESCRIPTOR = _TARGETMANUALCONTROLPARAMS,
  __module__ = 'actuated_pb2'
  # @@protoc_insertion_point(class_scope:targetManualControlParams)
  ))
_sym_db.RegisterMessage(targetManualControlParams)

targetAutoTimerParams = _reflection.GeneratedProtocolMessageType('targetAutoTimerParams', (_message.Message,), dict(
  DESCRIPTOR = _TARGETAUTOTIMERPARAMS,
  __module__ = 'actuated_pb2'
  # @@protoc_insertion_point(class_scope:targetAutoTimerParams)
  ))
_sym_db.RegisterMessage(targetAutoTimerParams)

targetAutoLuxParams = _reflection.GeneratedProtocolMessageType('targetAutoLuxParams', (_message.Message,), dict(
  DESCRIPTOR = _TARGETAUTOLUXPARAMS,
  __module__ = 'actuated_pb2'
  # @@protoc_insertion_point(class_scope:targetAutoLuxParams)
  ))
_sym_db.RegisterMessage(targetAutoLuxParams)

targetConfigurations = _reflection.GeneratedProtocolMessageType('targetConfigurations', (_message.Message,), dict(
  DESCRIPTOR = _TARGETCONFIGURATIONS,
  __module__ = 'actuated_pb2'
  # @@protoc_insertion_point(class_scope:targetConfigurations)
  ))
_sym_db.RegisterMessage(targetConfigurations)


# @@protoc_insertion_point(module_scope)