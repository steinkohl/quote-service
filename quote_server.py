import random
from concurrent import futures

import grpc
import requests

import quote_pb2
import quote_pb2_grpc


def _get_quotes_from_url(url: str) -> list:
    f = requests.get(url)
    if f.status_code == 404:
        raise ValueError
    lines = str(f.text).split("\n")
    return lines


def get_random_quote(
    url: str = "https://raw.githubusercontent.com/steinkohl/quotes/main/tech_quotes.txt",
) -> str:
    try:
        quotes = _get_quotes_from_url(url)
        return random.choice(quotes)
    except Exception as e:
        print("Error: ", e)
        return '"An error does not become a mistake until you refuse to correct it." - John F. Kennedy'


class QuoteServicer(quote_pb2_grpc.QuoteServiceServicer):
    def GetQuote(self, request, context):
        response = quote_pb2.QuoteReply()
        response.message = get_random_quote()


def main():
    server = grpc.server(futures.ThreadPoolExecutor())
    quote_pb2_grpc.add_QuoteServiceServicer_to_server(QuoteServicer(), server)
    server.add_insecure_port("[::]:50055")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    main()
