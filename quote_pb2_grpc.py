# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import quote_pb2 as quote__pb2


class QuoteServiceStub(object):
    """The quote service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetQuoteOfTheDay = channel.unary_unary(
                '/hipstershop.QuoteService/GetQuoteOfTheDay',
                request_serializer=quote__pb2.QuoteRequest.SerializeToString,
                response_deserializer=quote__pb2.QuoteReply.FromString,
                )


class QuoteServiceServicer(object):
    """The quote service definition.
    """

    def GetQuoteOfTheDay(self, request, context):
        """Sends a quote
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QuoteServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetQuoteOfTheDay': grpc.unary_unary_rpc_method_handler(
                    servicer.GetQuoteOfTheDay,
                    request_deserializer=quote__pb2.QuoteRequest.FromString,
                    response_serializer=quote__pb2.QuoteReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'hipstershop.QuoteService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class QuoteService(object):
    """The quote service definition.
    """

    @staticmethod
    def GetQuoteOfTheDay(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hipstershop.QuoteService/GetQuoteOfTheDay',
            quote__pb2.QuoteRequest.SerializeToString,
            quote__pb2.QuoteReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
