import json


def get_data_transactions(path):
    """функция возвращает список словарей с данными о  транзакциях"""
    try:
        with open(path, encoding="utf-8") as f:
            try:
                data_transactions = json.load(f)
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []
    return list(data_transactions)


# path = "C:/Users/Meira/PycharmProjects/card_client/data/operations.json"
# for transaction in get_data_transactions(path):
#     print(type(transaction))
