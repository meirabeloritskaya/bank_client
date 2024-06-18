import logging
from utils import get_data_transactions

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(
    "C:/Users/Meira/PycharmProjects/card_client/logs/currency_cod.log", encoding="utf-8"
)
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def currency_cod_transaction(transactions, currency_cod):
    """вывод транзакции, содержащей заданную валюту"""

    logger.info("поиск транзакции, содержащей заданную валюту")
    try:
        my_transactions = []
        for transaction in transactions:
            try:
                if "operationAmount" in transaction:
                    # Проверка валюты
                    if (
                        transaction["operationAmount"]["currency"]["code"]
                        == currency_cod
                    ):
                        logger.info("данный файл изначально был в формате JSON")
                        my_transactions.append(transaction)
                elif "currency_code" in transaction:
                    if transaction["currency_code"] == currency_cod:
                        logger.info("данный файл изначально  не был в формате JSON")
                        my_transactions.append(transaction)
                else:
                    logger.warning(f"Транзакция без нужных ключей: {transaction}")
            except Exception as e:
                logger.error(f"Неожиданная ошибка: {e} в транзакции: {transaction}")

        if my_transactions:
            return my_transactions
        else:
            return "Транзакций с такой валютой нет"

    except Exception as e:
        logger.error(f"Ошибка: {e}")
        return "Произошла ошибка при поиске валюты транзакции"


if __name__ == "__main__":
    path = "C:/Users/Meira/PycharmProjects/card_client/data/operations.json"
    list_trans = get_data_transactions(path)

    my_currency_cod = input("введите валюту транзакции RUB, USD, EUR: ")
    result = currency_cod_transaction(list_trans, my_currency_cod)
    if isinstance(result, str):
        print(result)
    else:
        print(*result, sep="\n")
