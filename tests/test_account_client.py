import pytest

from src.masks import account_client


@pytest.mark.parametrize(
    "number_user_card, expected", [(73654108430135874305, "**4305")]
)
def test_account_client(number_user_card, expected):
    assert account_client(number_user_card) == expected
