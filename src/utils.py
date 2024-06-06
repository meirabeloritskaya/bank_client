import json


def get_data_transactions(path):
    # функция возвращает список словарей с данными о  транзакциях
    try:
        with open(path, encoding="utf-8") as f:
            try:
                data_transactions = json.load(f)
            except json.JSONDecodeError as e:
                return [], str(e)
    except FileNotFoundError as e:
        return [], str(e)
    return data_transactions