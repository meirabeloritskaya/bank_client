import pytest


from src.widget import filter_alpha_data

from unittest.mock import MagicMock, patch

# Создаем заглушку (mock) для модуля masks
masks = MagicMock()

# Устанавливаем заглушку вместо реального модуля
with patch("src.widget.masks", masks):

    @pytest.mark.parametrize(
        "data_client, expected",
        [
            ("Visa Platinum 7000792289606361", "Visa Platinum"),
            ("Счет 73654108430135874305", "Счет"),
        ],
    )
    def test_filter_alpha_data(data_client, expected):
        assert filter_alpha_data(data_client) == expected
