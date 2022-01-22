import requests
import random


def _is_int(x):
    try:
        _int = int(x)
        return True
    except ValueError as e:
        return False


def _remove_line_count(lines: list) -> list:
    # remove the amount of lines, if given in first line
    if _is_int(lines[0]) and len(lines) > 0 and int(lines[0]) == len(lines) - 1:
        return lines[1:]
    return lines


def _get_quotes_from_url(url: str) -> list:
    f = requests.get(url)
    lines = str(f.text).split('\n')
    return _remove_line_count(lines)


def get_random_quote(
    url: str = "https://raw.githubusercontent.com/erossignon/qod4outlook/master/quotes.txt"
) -> str:
    try:
        quotes = _get_quotes_from_url(url)
        return random.choice(quotes)
    except:
        return '"An error does not become a mistake until you refuse to correct it." - John F. Kennedy'


print(get_random_quote())
