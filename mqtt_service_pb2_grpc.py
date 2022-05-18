# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import mqtt_service_pb2 as mqtt__service__pb2


class mqttStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.
        Args:
            channel: A grpc.Channel.
        """
        self.publish = channel.unary_unary(
                '/mqtt/publish',
                request_serializer=mqtt__service__pb2.mqtt_msg.SerializeToString,
                response_deserializer=mqtt__service__pb2.Empty.FromString,
                )


class mqttServicer(object):
    """Missing associated documentation comment in .proto file."""

    def publish(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_mqttServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'publish': grpc.unary_unary_rpc_method_handler(
                    servicer.publish,
                    request_deserializer=mqtt__service__pb2.mqtt_msg.FromString,
                    response_serializer=mqtt__service__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mqtt', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class mqtt(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def publish(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mqtt/publish',
            mqtt__service__pb2.mqtt_msg.SerializeToString,
            mqtt__service__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)