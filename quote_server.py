import random
import time
from concurrent import futures

import grpc
import requests
import logging

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
        return random.choice(quotes)  # nosec
    except Exception:
        return '"An error does not become a mistake until you refuse to correct it." - John F. Kennedy'


class QuoteServiceServicer(quote_pb2_grpc.QuoteServiceServicer):
    def GetQuoteOfTheDay(self, request, context):
        logging.info(f"Got new request: {request}")
        response = quote_pb2.QuoteReply()
        response.message = get_random_quote()
        logging.info(f"Send response: {response.message}")
        return response


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    quote_pb2_grpc.add_QuoteServiceServicer_to_server(QuoteServiceServicer(), server)
    server.add_insecure_port("[::]:50055")
    logging.info("Server initialized! Waiting for traffic...")
    server.start()

    # keep alive
    try:
        while True:
            time.sleep(10)
            logging.info("Server Running - Waiting for traffic...")
    except KeyboardInterrupt:
        server.stop(0)
