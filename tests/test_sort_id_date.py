import pytest

from src.processing import sort_id_date


@pytest.fixture
def id_state_date():
    return [
        {"id": 5, "state": "EXECUTED", "date": "2021-07-03"},
        {"id": 7, "state": "EXECUTED", "date": "2019-01-02"},
    ]


@pytest.mark.parametrize(
    "my_reverse, expected",
    [
        (
            True,
            [
                {"id": 5, "state": "EXECUTED", "date": "2021-07-03"},
                {"id": 7, "state": "EXECUTED", "date": "2019-01-02"},
            ],
        ),
        (
            False,
            [
                {"id": 7, "state": "EXECUTED", "date": "2019-01-02"},
                {"id": 5, "state": "EXECUTED", "date": "2021-07-03"},
            ],
        ),
    ],
)
def test_sort_id_date(id_state_date, my_reverse, expected):
    assert sort_id_date(id_state_date, my_reverse) == expected
