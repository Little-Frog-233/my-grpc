# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import sentiment_pb2 as sentiment__pb2


class SentimentStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSentiment = channel.unary_unary(
                '/sentiment.Sentiment/GetSentiment',
                request_serializer=sentiment__pb2.TextInput.SerializeToString,
                response_deserializer=sentiment__pb2.Results.FromString,
                )


class SentimentServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetSentiment(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SentimentServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSentiment': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSentiment,
                    request_deserializer=sentiment__pb2.TextInput.FromString,
                    response_serializer=sentiment__pb2.Results.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sentiment.Sentiment', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Sentiment(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetSentiment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentiment.Sentiment/GetSentiment',
            sentiment__pb2.TextInput.SerializeToString,
            sentiment__pb2.Results.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
