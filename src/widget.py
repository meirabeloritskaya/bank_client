import masks


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


def decoder_date(cod_date: str) -> str:
    """функция возвращает дату транзакции"""
    list_date = list(cod_date)[:10]
    revers_list_date = list_date[8:10] + list_date[5:7] + list_date[0:4]
    for i in (2, 5):
        revers_list_date.insert(i, ".")
    return "".join(revers_list_date)


number_card = filter_digital_data("Visa Platinum 7000792289606361")
number_account = filter_digital_data("Счет 73654108430135874305")

name_card = filter_alpha_data("Visa Platinum 7000792289606361")
name_account = filter_alpha_data("Счет 73654108430135874305")

digital_mask_cart = masks.card_client(number_card)
digital_mask_account = masks.account_client(number_account)

print(name_card, digital_mask_cart)
print(name_account, digital_mask_account)
print(decoder_date("2018-07-11T02:26:18.671407"))
