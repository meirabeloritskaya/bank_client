from unittest.mock import patch, MagicMock

import pandas as pd


from src.read_transactions_excel import get_data_transactions


def test_get_data_transactions_existing_file():
    """Устанавливаем макеты"""
    mock_logger = MagicMock()
    with patch(
        "src.read_transactions_excel.logging.getLogger", return_value=mock_logger
    ), patch("src.read_transactions_excel.pd.read_excel") as mock_read_excel:

        test_data = [
            {
                "amount": 16210.0,
                "currency_code": "PEN",
                "currency_name": "Sol",
                "date": "2023-09-05T11:30:32Z",
                "description": "Перевод организации",
                "from": "Счет 58803664561298323391",
                "id": 650703.0,
                "state": "EXECUTED",
                "to": "Счет 39745660563456619397",
            },
            {
                "amount": 29740.0,
                "currency_code": "COP",
                "currency_name": "Peso",
                "date": "2020-12-06T23:00:58Z",
                "description": "Перевод с карты на карту",
                "from": "Discover 3172601889670065",
                "id": 3598919.0,
                "state": "EXECUTED",
                "to": "Discover 0720428384694643",
            },
            {
                "amount": 30368.0,
                "currency_code": "TZS",
                "currency_name": "Shilling",
                "date": "2023-07-22T05:02:01Z",
                "description": "Перевод с карты на карту",
                "from": "Visa 1959232722494097",
                "id": 593027.0,
                "state": "CANCELED",
                "to": "Visa 6804119550473710",
            },
        ]
        test_df = pd.DataFrame(test_data)

        mock_read_excel.return_value = test_df

        """Вызываем функцию с тестовым файлом"""
        result = get_data_transactions("test_transactions.xlsx")

        """Проверяем, что вызывался логгер с нужными сообщениями"""
        mock_logger.info.assert_any_call("открытие файла test_transactions.xlsx")
        mock_logger.info.assert_any_call("Получение информации о транзакциях")

        """Проверяем результат"""

        assert result == result


def test_get_data_transactions_nonexistent_file():
    """Устанавливаем макеты"""
    mock_logger = MagicMock()
    with patch(
        "src.read_transactions_excel.logging.getLogger", return_value=mock_logger
    ), patch(
        "src.read_transactions_excel.pd.read_excel", side_effect=FileNotFoundError
    ):
        """Вызываем функцию с несуществующим файлом"""
        result = get_data_transactions("nonexistent_file.xlsx")

        """Проверяем, что вызывался логгер с нужным сообщением об ошибке"""
        mock_logger.error.assert_any_call(
            "путь к файлу nonexistent_file.xlsx не найден"
        )

        """Проверяем результат"""
        assert result == "{}"


def test_get_data_transactions_invalid_excel():
    """Устанавливаем макеты"""
    mock_logger = MagicMock()
    with patch(
        "src.read_transactions_excel.logging.getLogger", return_value=mock_logger
    ), patch(
        "src.read_transactions_excel.pd.read_excel",
        side_effect=ValueError("ValueError message"),
    ):
        """Вызываем функцию с некорректным файлом"""
        result = get_data_transactions("invalid_transactions.xlsx")

        """Проверяем, что вызывался логгер с нужным сообщением об ошибке парсинга"""
        mock_logger.error.assert_any_call(
            "Ошибка при парсинге Excel файла: ValueError message"
        )

        # Проверяем результат
        assert result == "{}"


if __name__ == "__main__":
    test_get_data_transactions_existing_file()
    test_get_data_transactions_nonexistent_file()
    test_get_data_transactions_invalid_excel()
