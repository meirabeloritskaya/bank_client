from src import masks


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
        if el.isalpha() or el == " ":
            alpha_data += el

    return alpha_data


def decoder_date(list_cod_date: str) -> str:
    """функция возвращает дату транзакции"""
    list_date = []
    for earch_date in list_cod_date:
        date_by_list = list(earch_date)[:10]
        revers_date_by_list = date_by_list[8:10] + date_by_list[5:7] + date_by_list[0:4]
        for i in (2, 5):
            revers_date_by_list.insert(i, ".")
        date_by_str = "".join(revers_date_by_list)
        list_date.append(date_by_str)
    return list_date


if __name__ == "__main__":
    number_card = filter_digital_data("Visa Platinum 7000792289606361")
    number_account = filter_digital_data("Счет 73654108430135874305")

    name_card = filter_alpha_data("Visa Platinum 7000792289606361")
    name_account = filter_alpha_data("Счет 73654108430135874305")

    digital_mask_cart = masks.card_client(number_card)
    digital_mask_account = masks.account_client(number_account)

    print(name_card, digital_mask_cart)
    print(name_account, digital_mask_account)
    my_list_cod_date = [
        "2018-07-11T02:26:18.671407",
        "2019-08-26T10:50:58.294041",
        "2018-01-13T13:00:58.458625",
    ]
    print(decoder_date(my_list_cod_date))
