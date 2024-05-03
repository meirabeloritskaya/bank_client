import widget


def card_client(number_user_card: int) -> str:
    """функция возвращает маску банковской карты клиента"""
    mask_list_card = list(str(number_user_card))
    for i in range(len(mask_list_card)):

        if i == 4 or i == 9 or i == 14:
            mask_list_card.insert(i, " ")

        if i in range(7, 9) or i in range(10, 14):
            mask_list_card[i] = "*"

    return "".join(mask_list_card)


def account_client(number_user_account: int) -> str:
    """функция возвращает маску банковского счета клмента"""
    mask_list_account = list(str(number_user_account))

    for i in range(0, 14):
        mask_list_account[i] = ""
    for i in range(14, 16):
        mask_list_account[i] = "*"

    return "".join(mask_list_account)


number_card = widget.filter_digital_data("Visa Platinum 7000792289606361")
number_account = widget.filter_digital_data("Счет 73654108430135874305")

name_card = widget.filter_alpha_data("Visa Platinum 7000792289606361")
name_account = widget.filter_alpha_data("Счет 73654108430135874305")

digital_mask_cart = card_client(number_card)
ditital_mask_account = account_client(number_account)

print(name_card, digital_mask_cart)
print(name_account, ditital_mask_account)
print(widget.decoder_date("2018-07-11T02:26:18.671407"))
