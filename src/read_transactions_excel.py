import json
import logging
import csv
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
    """функция возвращает список словарей с данными о  транзакциях"""
    try:
        logger.info("открытие файла transactions_excel.xlsx")
        try:
            logger.info("Получение информации о транзакциях")
            df = pd.read_excel(path)
            dict_df = df.to_dict(orient="records")
            return json.dumps(dict_df, indent=4)
        except pd.errors.ParserError as e:
            logger.error(f"Ошибка при парсинге Excel файла: {e}")
            return json.dumps({})
    except FileNotFoundError:
        logger.error("путь к файлу transactions_excel.xlsx не найден")
        return json.dumps({})


if __name__ == "__main__":
    path = "C:/Users/Meira/PycharmProjects/card_client/data/transactions_excel.xlsx"
    list_trans_json = get_data_transactions(path)

    print(list_trans_json)
