# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import servicio_pb2 as servicio__pb2


class SaludMentalStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.IsReady = channel.unary_unary(
                '/SaludMental/IsReady',
                request_serializer=servicio__pb2.Empty.SerializeToString,
                response_deserializer=servicio__pb2.Empty.FromString,
                )
        self.RegisterOrder = channel.unary_unary(
                '/SaludMental/RegisterOrder',
                request_serializer=servicio__pb2.Order.SerializeToString,
                response_deserializer=servicio__pb2.OrderConfirmation.FromString,
                )
        self.RegisterEncuesta = channel.unary_unary(
                '/SaludMental/RegisterEncuesta',
                request_serializer=servicio__pb2.Encuesta.SerializeToString,
                response_deserializer=servicio__pb2.EncuestaConfirmation.FromString,
                )


class SaludMentalServicer(object):
    """Missing associated documentation comment in .proto file."""

    def IsReady(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterEncuesta(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SaludMentalServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'IsReady': grpc.unary_unary_rpc_method_handler(
                    servicer.IsReady,
                    request_deserializer=servicio__pb2.Empty.FromString,
                    response_serializer=servicio__pb2.Empty.SerializeToString,
            ),
            'RegisterOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterOrder,
                    request_deserializer=servicio__pb2.Order.FromString,
                    response_serializer=servicio__pb2.OrderConfirmation.SerializeToString,
            ),
            'RegisterEncuesta': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterEncuesta,
                    request_deserializer=servicio__pb2.Encuesta.FromString,
                    response_serializer=servicio__pb2.EncuestaConfirmation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SaludMental', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SaludMental(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def IsReady(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SaludMental/IsReady',
            servicio__pb2.Empty.SerializeToString,
            servicio__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SaludMental/RegisterOrder',
            servicio__pb2.Order.SerializeToString,
            servicio__pb2.OrderConfirmation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterEncuesta(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SaludMental/RegisterEncuesta',
            servicio__pb2.Encuesta.SerializeToString,
            servicio__pb2.EncuestaConfirmation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
