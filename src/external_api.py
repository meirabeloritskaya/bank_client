import requests


from utils import get_data_transactions

path = "C:/Users/Meira/PycharmProjects/card_client/data/operations.json"


def amount_transaction(transaction_by_id):
    """функция возвращает сумму транзакции в рублях"""
    trans_amount = transaction_by_id["operationAmount"]["amount"]
    trans_code = transaction_by_id["operationAmount"]["currency"]["code"]
    headers_api = {"apikey": "5RYgssDSGX6KmJPkwfDSr3N2sva3wfT9"}

    if trans_code == "RUB":
        return trans_amount
    else:

        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={trans_code}&amount={trans_amount}"
        response = requests.request("GET", url, headers=headers_api)
        my_result = response.json()
        return my_result["result"]


for transaction in get_data_transactions(path):
    print(transaction)
