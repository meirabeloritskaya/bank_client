import logging
from datetime import datetime
from utils import get_data_transactions as set_json
from processing import select_state_id, sort_id_date
from read_transactions_csv import get_data_transactions as set_csv
from read_transactions_excel import get_data_transactions as set_excel
from currency_cod import currency_cod_transaction
from widget import decoder_date
from descriptions import description_transaction
from masks import card_client
from masks import account_client
from widget import filter_digital_data
from widget import filter_alpha_data

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(
    "C:/Users/Meira/PycharmProjects/card_client/logs/main.log", encoding="utf-8"
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
    """выбор формата файла  из JSON, CSV, XLSX"""
    while True:
        try:
            format_file = int(input())
            if format_file in range(1, 4):
                logger.info("выбран один из предложенных форматов")
                response_program = dict_response_program[format_file]
                print(response_program)
                return format_file
            else:
                logger.info("выбран неверный формат файла")
                print("Вы ввели неверный формат файла. Попробуйте снова!")
                print(choose_file)
        except Exception as e:
            logger.error(f"ошибка при выборе формаьа файла {e}")
            print("Что-то пошло не так! Попробуйте снова!")
            print(choose_file)


def read_file_by_format(format_file):
    """чтение выбраного формата файла"""
    logger.info("чтение выбраного формата файла")
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
    """вывод списка статусов транзакций"""
    logger.info("вывод списка статусов транзакций")
    set_states = set(
        transaction["state"] for transaction in transactions if "state" in transaction
    )
    my_list_state = []
    for state in set_states:
        if type(state) is str:
            my_list_state.append(state)
    print(f"Доступные для фильтрации статусы: {', '.join(my_list_state)}")
    return my_list_state


def choose_state(list_states):
    """выбор статуса транзакций для фильтрации"""
    logger.info("выбор статуса транзакций для фильтрации")
    while True:
        try:
            state = input(
                "Введите статус, по которому необходимо выполнить фильтрацию: "
            ).upper()

            if state in list_states:
                logger.info("выбран один из предложенных статусов транзакций")
                print(f"Операции отфильтрованы по статусу {state}")
                logger.info(f"Операции отфильтрованы по статусу {state}")
                return state
            else:
                logger.info(f"статус операции {state} недоступен")
                print(f"статус операции {state} недоступен. Попробуйте снова!")
                print(state)
        except Exception as e:
            logger.error(f"ошибка при выборе статуса транзакций {e}")
            print("Что-то пошло не так! Попробуйте снова!")
            print(state)


def list_date_transactions(transactions):
    """декодирование списка дат транзакций"""
    logger.info("декодирование списка дат транзакций")
    list_date = [el.get("date") for el in transactions if el.get("date")]
    my_format_date = decoder_date(list_date)
    return my_format_date


def update_dates(filter_by_state, list_date):
    """преобразование фоормата дат из отфильтрованных транзакций на формат  %d.%m.%Y"""
    logger.info(
        "преобразование фоормата дат из отфильтрованных транзакций на формат  %d.%m.%Y"
    )
    for i, transaction in enumerate(filter_by_state):
        if i < len(list_date):
            transaction["date"] = list_date[i]
    return filter_by_state


def rate_date(list_by_state):
    """преобразование фоормата дат из отфильтрованных транзакций на формат  %Y-%m-%d"""
    logger.info(
        "преобразование фоормата дат из отфильтрованных транзакций на формат  %Y-%m-%d"
    )
    try:
        logger.info("Преобразование дат в формат %Y-%m-%d")
        for el in list_by_state:
            el["date"] = datetime.strptime(el["date"], "%d.%m.%Y").strftime("%Y-%m-%d")

    except Exception as e:
        print(f"Что-то пошло не так: {e}")
        logger.error(f"Ошибка при преобразовании даты: {e}")
    return list_by_state


def sorted_by_date(transactions):
    """выбор сортировки по дате"""
    while True:
        try:
            sort_date = input("Отсортировать операции по дате? Да/Нет ").strip().title()

            if sort_date == "Да":
                logger.info("выбрана сортировка по дате")
                reverse_date = input(
                    "Отсортировать операции по возрастанию или убыванию даты? по возрастанию/по убыванию "
                )
                if reverse_date == "по возрастанию":
                    logger.info("выбрана сортировка по возрастанию")
                    sort_list_states = sort_id_date(transactions, reverse=False)
                    return sort_list_states
                elif reverse_date == "по убыванию":
                    logger.info("выбрана сортировка по убыванию")
                    sort_list_states = sort_id_date(transactions)
                    return sort_list_states
                else:
                    logger.info("Вы ввели некоректный ответ. Попробуйте снова.")
                    print("Вы ввели некоректный ответ. Попробуйте снова.")
                    print(reverse_date)

            elif sort_date == "Нет":
                logger.info("не выбрана сортировка по дате")
                return transactions

            else:
                logger.info("Введен некоректный ответ.")
                print("Вы ввели некоректный ответ. Попробуйте снова.")
                print(sort_date)
        except Exception as e:
            print(f"Что-то пошло не так: {e}")
            logger.error(f"Ошибка при сортировке по дате: {e}")
            print(sort_date)


def filter_by_currency_cod(transactions):
    """выбор валюты транзакций для фильтрации"""
    logger.info("выбор валюты транзакций для фильтрации")
    while True:
        try:
            is_cod_rub = (
                input("Выводить только рублевые транзакции? Да/Нет: ").strip().title()
            )

            if is_cod_rub == "Да":
                logger.info("выбраны рублевые транзакции")
                transactions_rub = currency_cod_transaction(transactions, "RUB")
                return transactions_rub
            elif is_cod_rub == "Нет":
                logger.info("выбраны все транзакции")
                return transactions

            else:
                logger.info("Введен некоректный ответ.")
                print("Вы ввели некоректный ответ. Попробуйте снова.")
                print(is_cod_rub)
        except Exception as e:
            print(f"Что-то пошло не так: {e}")
            logger.error(f"Ошибка при фильтрации: {e}")
            print(is_cod_rub)


def filter_by_word(transactions):
    """выбор слова в описании для фильтрации"""
    logger.info("выбор слова в описании для фильтрации")
    while True:
        try:
            is_word_description = (
                input(
                    "Отфильтровать список транзакций по определенному слову? Да/Нет: "
                )
                .strip()
                .title()
            )

            if is_word_description == "Да":
                logger.info("выбрано слово в описании")
                word_description = input(
                    "введите слово или фразу, которые должно находиться в описании транзакции: "
                )
                list_filter_by_word = description_transaction(
                    transactions, word_description
                )
                # print('Распечатываю итоговый список транзакций...')
                return list_filter_by_word

            elif is_word_description == "Нет":
                logger.info("слово в описании не выбрано")
                print("Распечатываю итоговый список транзакций...")
                return transactions

            else:
                logger.info("Введен некоректный ответ.")
                print("Вы ввели некоректный ответ. Попробуйте снова.")
                print(is_word_description)
        except Exception as e:
            print(f"Что-то пошло не так: {e}")
            logger.error(f"Ошибка при фильтрации: {e}")
            print(is_word_description)


def mask_list_by_from_to(transactions):
    masked_transactions = []
    for transaction in transactions:
        masked_transaction = transaction.copy()
        if "from" in transaction and isinstance(transaction["from"], str):
            if "счет" in transaction["from"].lower():
                number_account = filter_digital_data(transaction["from"])
                name_account = filter_alpha_data(transaction["from"])
                digital_mask_account = account_client(number_account)
                masked_transaction["from"] = f"{name_account} {digital_mask_account}"
            else:
                number_card = filter_digital_data(transaction["from"])
                name_card = filter_alpha_data(transaction["from"])
                digital_mask_card = card_client(number_card)
                masked_transaction["from"] = f"{name_card} {digital_mask_card}"

        if "to" in transaction and isinstance(transaction["to"], str):
            if "счет" in transaction["to"].lower():
                number_account = filter_digital_data(transaction["to"])
                name_account = filter_alpha_data(transaction["to"])
                digital_mask_account = account_client(number_account)
                masked_transaction["to"] = f"{name_account} {digital_mask_account}"
            else:
                number_card = filter_digital_data(transaction["to"])
                name_card = filter_alpha_data(transaction["to"])
                digital_mask_card = card_client(number_card)
                masked_transaction["to"] = f"{name_card} {digital_mask_card}"

        masked_transactions.append(masked_transaction)
    return masked_transactions


def len_transactions(transactions):
    num_transactions = len(transactions)
    return f"Всего банковских операций: {num_transactions}"


def print_transaction(transactions):
    """вывод транзакций в нужном виде"""
    logger.info("ввывод транзакций в нужном виде")
    print("-" * 30)
    for transaction in transactions:
        print(f"{transaction['date']}  {transaction['description']}")
        try:
            print(f"{transaction['from']} -> {transaction['to']}")
            if transaction["from"] == None:
                print(f"-> {transaction['to']}")
        except Exception as e:
            print(e)
        try:
            if "operationAmount" in transaction:
                print(
                    f"Сумма: {transaction['amount']} {transaction["operationAmount"]["currency"]["code"]}"
                )
            elif "currency_code" in transaction:
                print(f"Сумма: {transaction['amount']} {transaction["currency_code"]}")
            else:
                logger.warning(f"Транзакция без нужных ключей: {transaction}")
        except Exception as e:
            logger.error(f"Неожиданная ошибка: {e} в транзакции: {transaction}")
        print("-" * 30)


if __name__ == "__main__":
    my_format_file = format_file()
    my_list_trans = read_file_by_format(my_format_file)
    my_list_states = set_by_state(my_list_trans)
    my_state = choose_state(my_list_states)

    my_filter_by_state = select_state_id(my_list_trans, my_state)
    # print(*my_filter_by_state, sep="\n")
    my_list_date = list_date_transactions(my_filter_by_state)
    # print(my_list_date)
    my_list_transactions_by_state = update_dates(my_filter_by_state, my_list_date)
    # print(*my_list_transactions_by_state, sep='\n')
    my_list_norm_format_date = rate_date(my_list_transactions_by_state)
    # print(*my_list_norm_format_date, sep='\n')
    my_sorted_list_transactions = sorted_by_date(my_list_norm_format_date)
    # print(*my_sorted_list_transactions, sep="\n")
    my_list_filter_by_currency_cod = filter_by_currency_cod(my_sorted_list_transactions)
    # print(*my_list_filter_by_currency_cod, sep='\n')
    my_list_filter_by_word = filter_by_word(my_list_filter_by_currency_cod)
    # print(*my_list_filter_by_word, sep='\n')
    my_mask_list = mask_list_by_from_to(my_list_filter_by_word)
    # print(*my_mask_list, sep='\n')
    print(len_transactions(my_mask_list))
    print_transaction(my_mask_list)
