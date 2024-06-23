import logging
import re
from utils import get_data_transactions

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(
    "C:/Users/Meira/PycharmProjects/card_client/logs/descriptions.log", encoding="utf-8"
)
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def description_transaction(transactions, my_string):
    """вывод транзакции, содержащей заданное описание"""
    logger.info("поиск транзакции, содержащей заданное описание")
    try:
        pattern = re.compile(rf"{re.escape(my_string)}", re.IGNORECASE)
        my_transactions = []
        for transaction in transactions:
            try:
                if pattern.search(transaction["description"]):
                    logger.debug(
                        f"Найдено совпадение в транзакции: {transaction['id']}"
                    )
                    my_transactions.append(transaction)

            except KeyError as ke:
                logger.error(f"Ошибка KeyError: {ke} в транзакции: {transaction}")
            except Exception as e:
                logger.error(f"Неожиданная ошибка: {e} в транзакции: {transaction}")

        if my_transactions:
            return my_transactions
        else:
            return "Такого описания нет"

    except Exception as e:
        logger.error(f"Ошибка: {e}")
        return "Произошла ошибка при поиске описания"


if __name__ == "__main__":
    path = "C:/Users/Meira/PycharmProjects/card_client/data/operations.json"
    list_trans = get_data_transactions(path)
    my_string = input(
        "введите слово или фразу, которые должно находиться в описании транзакции: "
    )
    print(*description_transaction(list_trans, my_string), sep="\n")
