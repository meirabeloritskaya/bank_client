from unittest.mock import mock_open, patch
from src.utils import get_data_transactions


def test_successful_read():
    '''проверяем, что файл json корректно читается'''
    mock_data = ('[{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041", "operationAmount": '
                 '{"amount": "31957.58", "currency": '
                 '{"name": "руб.", "code": "RUB"}}}]')
    with patch("builtins.open", mock_open(read_data=mock_data)):
        data = get_data_transactions("pass_to_file_json")
        assert data == [
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                    "amount": "31957.58",
                    "currency": {"name": "руб.", "code": "RUB"},
                },
            }
        ]
        print("test_successful_read")

def test_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        data = get_data_transactions("non_existent_file.json")
        assert data == []
        print("test_file_not_found passed")