import logging

import pandas as pd

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(
    "C:/Users/Meira/PycharmProjects/card_client/logs/read_transactions_excel_xlsx.log",
    encoding="utf-8",
)
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_data_transactions(path):
    logger = logging.getLogger(__name__)
    try:
        df = pd.read_excel(path)
        logger.info(f"открытие файла {path}")
        logger.info("Получение информации о транзакциях")
        return df.to_dict(orient="records")
    except FileNotFoundError:
        logger.error(f"путь к файлу {path} не найден")
        return "{}"
    except ValueError as e:
        logger.error(f"Ошибка при парсинге Excel файла: {str(e)}")
        return "{}"


if __name__ == "__main__":
    path = "C:/Users/Meira/PycharmProjects/card_client/data/transactions_excel.xlsx"
    list_trans_json = get_data_transactions(path)

    print(list_trans_json)
