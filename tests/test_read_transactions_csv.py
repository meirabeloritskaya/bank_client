import os
import pandas as pd

from src.read_transactions_csv import get_data_transactions


def setup_function():
    """Настройка для тестирования"""
    global data, csv_path, df
    data = [
        {"id": 1, "state": "EXECUTED", "amount": 100},
        {"id": 2, "state": "PENDING", "amount": 200},
        {"id": 3, "state": "CANCELED", "amount": 300},
    ]
    csv_path = "test_transactions.csv"
    df = pd.DataFrame(data)
    df.to_csv(csv_path, sep=";", index=False)


def teardown_function():
    """Очистка после тестирования"""
    os.remove(csv_path)


def test_get_data_transactions_existing_file():
    """Тестирование чтения существующего файла"""
    result = get_data_transactions(csv_path)
    assert isinstance(result, pd.DataFrame)
    assert len(result) == len(data)


def test_get_data_transactions_nonexistent_file():
    """Тестирование обработки ошибки при отсутствии файла"""
    result = get_data_transactions("nonexistent_file.csv")
    assert isinstance(result, pd.DataFrame)
    assert result.empty


def test_get_data_transactions_invalid_csv():
    """Тестирование обработки ошибки при некорректном CSV"""
    invalid_csv_path = "invalid_transactions.csv"
    with open(invalid_csv_path, "w", encoding="utf-8") as f:
        f.write("id;state;amount\n")  # Некорректный разделитель

    result = get_data_transactions(invalid_csv_path)
    assert isinstance(result, pd.DataFrame)
    assert result.empty

    os.remove(invalid_csv_path)


if __name__ == "__main__":
    setup_function()
    test_get_data_transactions_existing_file()
    test_get_data_transactions_nonexistent_file()
    test_get_data_transactions_invalid_csv()
    teardown_function()
