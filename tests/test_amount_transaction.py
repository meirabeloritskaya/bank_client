from unittest.mock import patch
from src.external_api import amount_transaction
import requests


def test_amount_transaction_rub():
    """Проверяем, что транзакция в рублях корректно обрабатывается"""
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {"name": "руб.", "code": "RUB"},
        },
    }
    amount = amount_transaction(transaction)
    assert amount == "31957.58"
    print("test_amount_transaction_rub")


@patch("requests.request")
def test_amount_transaction_other_currency(mock_request):
    """Проверяем, что транзакция в другой валюте корректно обрабатывается"""
    transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {"name": "USD", "code": "USD"},
        },
    }
    mock_response = mock_request.return_value
    mock_response.json.return_value = {"result": 7200.00}

    amount = amount_transaction(transaction)
    assert amount == 7200.00
    mock_request.assert_called_once()
    args, kwargs = mock_request.call_args
    assert args[0] == "GET"
    assert "apikey=test_api_key" in kwargs["headers"].values()
    assert (
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100.00"
        in args
    )
    print("test_amount_transaction_other_currency passed")
