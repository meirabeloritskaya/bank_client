import logging

from utils import get_data_transactions as set_json
from processing import select_state_id, sort_id_date
from read_transactions_csv import get_data_transactions as set_csv
from read_transactions_excel import get_data_transactions as set_excel
from widget import decoder_date

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


print(
    """Привет! 
Добро пожаловать в программу работы с банковскими транзакциями."""
)
choose_file = """Выберите необходимый пункт меню:
      1. Получить информацию о транзакциях из JSON-файла
      2. Получить информацию о транзакциях из CSV-файла
      3. Получить информацию о транзакциях из XLSX-файла: """
print(choose_file)

dict_response_program = {
    1: "Для обработки выбран JSON-файл",
    2: "Для обработки выбран CSV-файл",
    3: "Для обработки выбран XLSX-файл",
}


def format_file():
    while True:
        try:
            format_file = int(input())
            if format_file in range(1, 4):
                response_program = dict_response_program[format_file]
                print(response_program)
                return format_file
            else:
                print("Вы ввели неверный формат файла. Попробуйте снова!")
                print(choose_file)
        except ValueError:
            print("Вы ввели неверный формат файла. Попробуйте снова!")
            print(choose_file)


def read_file_by_format(format_file):
    if format_file == 1:
        path = "C:/Users/Meira/PycharmProjects/card_client/data/operations.json"
        list_trans_json = set_json(path)
        return list_trans_json
    elif format_file == 2:
        path = "C:/Users/Meira/PycharmProjects/card_client/data/transactions.csv"
        list_trans_csv = set_csv(path)
        return list_trans_csv
    elif format_file == 3:
        path = "C:/Users/Meira/PycharmProjects/card_client/data/transactions_excel.xlsx"
        list_trans_excel = set_excel(path)
        return list_trans_excel


def set_by_state(transactions):
    set_states = set(
        transaction["state"] for transaction in transactions if "state" in transaction
    )
    my_list_state = []
    for state in set_states:
        if type(state) == str:
            my_list_state.append(state)
    print(f"Доступные для фильтрации статусы: {', '.join(my_list_state)}")
    return my_list_state


def choose_state(list_states):
    while True:
        try:
            state = input(
                "Введите статус, по которому необходимо выполнить фильтрацию: "
            )
            if state in list_states:
                state_upper = state.upper()
                print(f"Операции отфильтрованы по статусу {state}")
                return state_upper
            else:
                print(f"статус операции {state} недоступен.")
                print(state)
        except ValueError:
            print(f"статус операции {state} недоступен.")
            print(state)


if __name__ == "__main__":
    my_format_file = format_file()
    my_list_trans = read_file_by_format(my_format_file)
    my_list_states = set_by_state(my_list_trans)
    my_state = choose_state(my_list_states)
    my_format_date = decoder_date()
    my_filter_by_state = select_state_id(my_list_trans, my_state)
    print(*my_filter_by_state, sep="\n")
