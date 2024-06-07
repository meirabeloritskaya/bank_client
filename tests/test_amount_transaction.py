import requests
import os

from src.utils import get_data_transactions
from src.external_api import amount_transaction
from dotenv import load_dotenv
from unittest.mock import patch


load_dotenv("C:/Users/Meira/PycharmProjects/card_client/.env")
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

#
# @patch("requests.get")
# def test_amount_transaction_other_currency(mock_get):
#     """Проверяем, что транзакция в другой валюте корректно обрабатывается"""
#     transaction = {
#         "id": 41428829,
#         "state": "EXECUTED",
#         "date": "2019-07-03T18:35:29.512364",
#         "operationAmount": {
#             "amount": "8221.37",
#             "currency": {"name": "USD", "code": "USD"},
#         },
#     }
#     mock_get.return_value.json.return_value = {"result": 529018.10}
#
#
#     amount = amount_transaction(transaction)
#     assert amount == 529018.10
#     mock_get.assert_called_once()
#
#     print("test_amount_transaction_other_currency")

if __name__ == "__main__":
    test_amount_transaction_rub()
    # test_amount_transaction_other_currency()