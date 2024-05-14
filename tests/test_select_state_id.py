import pytest

from src.processing import select_state_id


@pytest.fixture
def id_state_date():
    return [
        {"id": 5, "state": "EXECUTED", "date": "2021-07-03"},
        {"id": 6, "state": "CANCELED", "date": "2021-09-08"},
        {"id": 7, "state": "EXECUTED", "date": "2019-01-02"},
        {"id": 8, "state": "CANCELED", "date": "2014-07-01"},
    ]


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 5, "state": "EXECUTED", "date": "2021-07-03"},
                {"id": 7, "state": "EXECUTED", "date": "2019-01-02"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 6, "state": "CANCELED", "date": "2021-09-08"},
                {"id": 8, "state": "CANCELED", "date": "2014-07-01"},
            ],
        ),
    ],
)
def test_select_state_id(id_state_date, state, expected):
    assert select_state_id(id_state_date, state) == expected
