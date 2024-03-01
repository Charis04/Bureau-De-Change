import pytest
import os
from main import download_rates
from main import get_exchange_rate
from main import convert


def test_download_rates():
    download_rates("exchange.csv")
    assert os.path.exists("exchange.csv")


def test_get_exchange_rate():
    assert type(get_exchange_rate("exchange.csv", 'to naira', 'usd')) is float


def test_convert():
    assert convert('to naira', 2, 5) == 10.0