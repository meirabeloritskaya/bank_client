import pytest


from src.widget import filter_digital_data

from unittest.mock import MagicMock, patch

# Создаем заглушку (mock) для модуля masks
masks = MagicMock()

# Устанавливаем заглушку вместо реального модуля
with patch('src.masks', masks):
     @pytest.mark.parametrize(
       "data_client, expected",
        [("Visa Platinum 7000792289606361", 7000792289606361),
       ("Счет 73654108430135874305", 73654108430135874305)])

     def test_filter_digital_data(data_client, expected):
       assert filter_digital_data(data_client) == expected



