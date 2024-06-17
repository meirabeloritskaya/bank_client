import logging

from utils import get_data_transactions
from collections import Counter

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


def list_categories(transactions):

    return (
        transaction["description"]
        for transaction in transactions
        if "description" in transaction
    )


def categories_by_descriptions(transactions, my_list_categories):

    counted = Counter(my_list_categories)
    return counted


if __name__ == "__main__":
    path = "C:/Users/Meira/PycharmProjects/card_client/data/operations.json"
    list_trans = get_data_transactions(path)
    # print(*list_categories(list_trans), sep="\n")
    my_list_categories = list_categories(list_trans)
    print(categories_by_descriptions(list_trans, my_list_categories))
