def filter_digital_data(data_client: str) -> int:
    """функция возвращает только цифровые значения карты или счета"""
    digital_data = ""

    for el in list(data_client):
        if el.isdigit():
            digital_data += el

    return int(digital_data)


def filter_alpha_data(data_client: str):
    """функция возвращает только название карты или счета"""
    alpha_data = ""

    for el in list(data_client):
        if el.isalpha():
            alpha_data += el

    return alpha_data


def filter_type_data(data_client):
    """функция распознает: являются ли введенные данные  номером карты или счета"""
    if len(data_client) == 16:
        digital_card = data_client

    if len(data_client) == 20:
        digital_account = data_client

    return digital_card, digital_account


def decoder_date(cod_date: str) -> str:
    """функция возвращает дату транзакции"""
    list_date = list(cod_date)[:10]
    revers_list_date = list_date[8:10] + list_date[5:7] + list_date[0:4]
    for i in (2, 5):
        revers_list_date.insert(i, ".")
    return "".join(revers_list_date)
