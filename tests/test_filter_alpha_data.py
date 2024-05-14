import pytest


from src.widget import filter_alpha_data


@pytest.mark.parametrize(
    "data_client, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum "),
        ("Счет 73654108430135874305", "Счет "),
    ],
)
def test_filter_alpha_data(data_client, expected):
    assert filter_alpha_data(data_client) == expected
