from datetime import datetime
from utils import get_data_transactions


def select_state_id(list_trans: list, state: str) -> list:
    """функция возвращет список id по заданным state"""

    list_id = list(filter(lambda el: el.get("state") == state, list_trans))
    return list_id


def sort_id_date(list_id: list, reverse=True) -> list:
    """функция сортирует список id по date"""

    return sorted(
        list_id,
        key=lambda el: datetime.strptime(el["date"], "%Y-%m-%d"),
        reverse=reverse,
    )


if __name__ == "__main__":
    # path = "C:/Users/Meira/PycharmProjects/card_client/data/operations.json"
    # list_trans = get_data_transactions(path)
    list_state_id = [
        {"id": 1, "state": "EXECUTED", "date": "2021-07-03"},
        {"id": 2, "state": "CANCELED", "date": "2014-07-03"},
        {"id": 3, "state": "EXECUTED", "date": "2019-01-03"},
        {"id": 4, "state": "CANCELED", "date": "2010-07-03"},
    ]

    new_list_id = select_state_id(list_state_id, "CANCELED")
    print(new_list_id)
    print(sort_id_date(new_list_id))
