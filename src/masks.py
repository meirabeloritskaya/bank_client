def card_client(number_card: int) -> str:
    """функция возвращает маску банковской карты клиента"""
    mask_list_card = list(str(number_card))
    for i in range(len(mask_list_card)):

        if i == 4 or i == 9 or i == 14:
            mask_list_card.insert(i, " ")

        if i in range(7, 9) or i in range(10, 14):
            mask_list_card[i] = "*"

    return "".join(mask_list_card)


def account_client(number_account: int) -> str:
    """функция возвращает маску банковского счета клмента"""
    mask_list_account = list(str(number_account))

    for i in range(0, 14):
        mask_list_account[i] = ""
    for i in range(14, 16):
        mask_list_account[i] = "*"

    return "".join(mask_list_account)


def filter_digital_data(data_client: str) -> int:
    """функция возвращает только цифровые значения карты или счета"""
    digital_data = ""

    for el in list(data_client):
        if el.isdigit():
            digital_data += el

    return int(digital_data)

def filter_alpha_data(data_client: str):
    "функция возвращает только название карты или счета"
    alpha_data = ""

    for el in list(data_client):
        if el.isalpha():
            alpha_data += el

    return alpha_data


def filter_type_data(data_client):
    """функция распознает: являются ли  введенные данные  номером карты или счета"""
    if len(data_client) == 16:
        digital_card = data_client

    if len(data_client) == 20:
        digital_account = data_client

    return digital_card, digital_account

def decoder_date(cod_data: str) -> str:
    """функция возвращает дату транзакции"""
    list_date = list(cod_data)[:10]
    revers_list_date = list_date[8:10] + list_date[5:7] + list_date[0:4]
    for i in (2, 5):
        revers_list_date.insert(i, ".")
    return "".join(revers_list_date)



number_card = filter_digital_data("Visa Platinum 7000792289606361")
number_account = filter_digital_data("Счет 73654108430135874305")

name_card = filter_alpha_data("Visa Platinum 7000792289606361")
name_account = filter_alpha_data("Счет 73654108430135874305")

digital_mask_cart = card_client(number_card)
ditital_mask_account = account_client(number_account)

print(name_card, digital_mask_cart)
print(name_account, ditital_mask_account)
print(decoder_date("2018-07-11T02:26:18.671407"))
