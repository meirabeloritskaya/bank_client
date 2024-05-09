

from datetime import datetime


def select_state_id(list_state_id: list, state: str = "EXECUTED") -> list:
    """функция возвращет список id по заданным state"""
    list_id = list(filter(lambda el: el["state"] == state, list_state_id))
    return list_id


list_state_id = [
    {"id": 1, "state": "EXECUTED", "date": "2021-07-03"},
    {"id": 2, "state": "CANCELED", "date": "2014-07-03"},
    {"id": 3, "state": "EXECUTED", "date": "2019-01-03"},
    {"id": 4, "state": "CANCELED", "date": "2010-07-03"},
]


def sort_id_by_date(list_id: list, reverse=True) -> list:
    """функция сортирует список id по date"""
    return sorted(
        list_id,
        key=lambda el: datetime.strptime(el["date"], "%Y-%m-%d"),
        reverse=reverse,
    )


new_list_id = select_state_id(list_state_id, "CANCELED")
print(new_list_id)
print(sort_id_by_date(new_list_id))
