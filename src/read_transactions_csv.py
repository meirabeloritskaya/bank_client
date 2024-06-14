import logging
import csv

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(
    "C:/Users/Meira/PycharmProjects/card_client/logs/read_transactions_csv.log",
    encoding="utf-8",
)
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_data_transactions(path):
    """функция возвращает список словарей с данными о  транзакциях"""
    try:
        logger.info("открытие файла transactions.csv")
        with open(path, encoding="utf-8") as f:
            try:
                logger.info("Получение информации о транзакциях")
                reader = csv.DictReader(f, delimiter=";")

                data_transactions = [row for row in reader]
            except csv.Error as e:
                logger.error(f"Ошибка чтения CSV файла: {e}")
                return []
    except FileNotFoundError:
        logger.error("путь к файлу transactions.csv не найден")
        return []
    return data_transactions


if __name__ == "__main__":
    path = "C:/Users/Meira/PycharmProjects/card_client/data/transactions.csv"
    list_trans = get_data_transactions(path)
    for trans in list_trans:
        for key, value in trans.items():
            print(f"{key}: {value}")
        print("\n")
