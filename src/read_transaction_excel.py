import logging
import csv

import pandas as pd

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(
    "C:/Users/Meira/PycharmProjects/card_client/logs/read_transactions_excel.xlsx.log",
    encoding="utf-8",
)
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_data_transactions(path, n):
    """функция возвращает список словарей с данными о  транзакциях"""
    try:
        logger.info("открытие файла transactions.excel.xlsx")
        with open(path, encoding="utf-8") as f:
            try:
                logger.info("Получение информации о транзакциях")
                reader = pd.read_csv(f, delimiter=";")
                print(reader.shape)
                print(reader.head(n))

            except csv.Error as e:
                logger.error(f"Ошибка чтения CSV файла: {e}")
                return []
    except FileNotFoundError:
        logger.error("путь к файлу transactions.excel.xlsx не найден")
        return []
    return reader


if __name__ == "__main__":
    path = "C:/Users/Meira/PycharmProjects/card_client/data/transactions.excel.xlsx"
    list_trans = get_data_transactions(path, 6)
