import pytest


from src.widget import decoder_date

# from unittest.mock import MagicMock, patch
#
# # Создаем заглушку (mock) для модуля masks
# masks = MagicMock()
#
# # Устанавливаем заглушку вместо реального модуля
# with patch('src.masks', masks):
@pytest.mark.parametrize(
       "cod_date, expected",
       [("2018-07-11T02:26:18.671407", "11.07.2018")])

def test_decoder_date(cod_date, expected):
       assert decoder_date(cod_date) == expected

