import unittest
from unittest import TestCase, mock

from quote_server import get_random_quote


def mock_get_quotes_from_url(values):
    return ['"This is a mocked quote." - Unit Tester']


class Test(TestCase):

    @mock.patch("quote_server._get_quotes_from_url", mock_get_quotes_from_url)
    def test_get_random_quote(self):
        actual = get_random_quote()
        expected = '"This is a mocked quote." - Unit Tester'
        self.assertEqual(expected, actual)

    def test_get_random_quote_invalid_url(self):
        actual = get_random_quote("invalid_url")
        expected = '"An error does not become a mistake until you refuse to correct it." - John F. Kennedy'
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
