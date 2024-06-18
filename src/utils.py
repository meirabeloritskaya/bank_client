import json
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(
    "C:/Users/Meira/PycharmProjects/card_client/logs/utils.log", encoding="utf-8"
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
        logger.info("открытие файла operations.json")
        with open(path, encoding="utf-8") as f:
            try:
                logger.info("Получение информации о транзакциях")
                data_transactions = json.load(f)

            except json.JSONDecodeError:
                logger.error("невозможно декодировать файл operations.json")
                return []
    except FileNotFoundError:
        logger.error("путь к файлу operations.json не найден")
        return []
    return data_transactions


if __name__ == "__main__":
    path = "C:/Users/Meira/PycharmProjects/card_client/data/operations.json"
    list_trans = get_data_transactions(path)
    # n = int(input("введите количество транзакций: "))
    # for i in range(n):
    #     print(list_trans[i])
    print(type(list_trans))
    print(*list_trans, sep="\n")
