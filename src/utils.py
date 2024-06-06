import json


def get_data_transactions(path):
    """функция возвращает список словарей с данными о  транзакциях"""
    try:
        with open(path, encoding="utf-8") as f:
            try:
                data_transactions = json.load(f)
            except json.JSONDecodeError as e:
                return []
    except FileNotFoundError as e:
        return []
    return data_transactions


# path = "C:/Users/Meira/PycharmProjects/card_client/data/operations.json"
