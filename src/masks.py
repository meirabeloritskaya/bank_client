import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(
    "C:/Users/Meira/PycharmProjects/card_client/logs/masks.log", encoding="utf-8"
)
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def card_client(number_user_card: int) -> str:
    """функция возвращает маску банковской карты клиента"""
    logger.info("маскируем банковскую карту клиента")
    mask_list_card = list(str(number_user_card))
    for i in range(len(mask_list_card)):

        if i == 4 or i == 9 or i == 14:
            mask_list_card.insert(i, " ")

        if i in range(7, 9) or i in range(10, 14):
            mask_list_card[i] = "*"

    return "".join(mask_list_card)


def account_client(number_user_account: int) -> str:
    """функция возвращает маску банковского счета клмента"""
    logger.info("маскируем банковский счет клиента")
    mask_list_account = list(str(number_user_account))

    for i in range(0, 14):
        mask_list_account[i] = ""
    for i in range(14, 16):
        mask_list_account[i] = "*"

    return "".join(mask_list_account)


if __name__ == "__main__":
    card_client(1596837868705199)
    account_client(64686473678894779589)
