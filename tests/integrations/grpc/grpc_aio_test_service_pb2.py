# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_aio_test_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1bgrpc_aio_test_service.proto\x12\x14grpc_aio_test_server""\n\x12gRPCaioTestMessage\x12\x0c\n\x04text\x18\x01 \x01(\t2u\n\x12gRPCaioTestService\x12_\n\tTestServe\x12(.grpc_aio_test_server.gRPCaioTestMessage\x1a(.grpc_aio_test_server.gRPCaioTestMessageb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "grpc_aio_test_service_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _globals["_GRPCAIOTESTMESSAGE"]._serialized_start = 53
    _globals["_GRPCAIOTESTMESSAGE"]._serialized_end = 87
    _globals["_GRPCAIOTESTSERVICE"]._serialized_start = 89
    _globals["_GRPCAIOTESTSERVICE"]._serialized_end = 206
# @@protoc_insertion_point(module_scope)