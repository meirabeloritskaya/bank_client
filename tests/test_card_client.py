import pytest

from src.masks import card_client


@pytest.mark.parametrize(
    "number_user_card, expected", [(7000792289606361, "7000 79** **** 6361")]
)
def test_card_client(number_user_card, expected):
    assert card_client(number_user_card) == expected
