from concurrent import futures
import requests
import random
import grpc
import quote_pb2
import quote_pb2_grpc


def _get_quotes_from_url(url: str) -> list:
    f = requests.get(url)
    lines = str(f.text).split('\n')
    return lines


def get_random_quote(
    url: str = "https://raw.githubusercontent.com/steinkohl/quotes/main/tech_quotes.txt"
) -> str:
    try:
        quotes = _get_quotes_from_url(url)
        # maybe '404: Not Found' as return?
        if len(quotes) == 1 and str(quotes[0]).startswith('404'):
            return "Error 404: Quote not found"
        return random.choice(quotes)
    except Exception:
        return '"An error does not become a mistake until you refuse to correct it." - John F. Kennedy'


class QuoteServicer(quote_pb2_grpc.QuoteServiceServicer):
    def GetQuote(self, request, context):
        response = quote_pb2.QuoteReply()
        response.message = get_random_quote()


def main():
    server = grpc.server(futures.ThreadPoolExecutor())
    quote_pb2_grpc.add_QuoteServiceServicer_to_server(QuoteServicer(), server)
    server.add_insecure_port('[::]:50055')
    server.start()
    server.wait_for_termination()


main()
