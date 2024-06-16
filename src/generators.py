def filter_by_currency(my_list_dict_transact, my_currency):
    """итератор, который выдает по очереди операции, в которых указана заданная валюта"""

    my_currency_transactions = (
        x
        for x in my_list_dict_transact
        if x["operationAmount"]["currency"]["code"] == my_currency
    )
    yield from my_currency_transactions


def transaction_descriptions(my_list_dict_transact):
    """генератор, который принимает список словарей и возвращает описание каждой операции по очереди"""
    for transaction in my_list_dict_transact:
        yield transaction["description"]


def card_number_generator(start, end):
    """генератор номеров банковских карт"""
    for num in range(start, end + 1):
        add_zeros = str(num).zfill(16)
        card_number = " ".join(
            [add_zeros[i : i + 4] for i in range(0, len(add_zeros), 4)]
        )
        yield card_number


if __name__ == "__main__":
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {"name": "руб.", "code": "EUR"},
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]

    n = int(input("введите колличество генерируемых номеров карточек: "))
    for card_number in card_number_generator(1, n):
        print(card_number)

    my_currency = input("\nmy_currency: ").strip().upper()
    count_transactions = int(input("count_transactions: "))
    my_currency_transactions = filter_by_currency(transactions, my_currency)
    try:
        for i in range(count_transactions):
            transaction = next(my_currency_transactions)
            print(f'\nоперация с  {my_currency}: {transaction["id"]}')
    except StopIteration:
        print(f"других операций с {my_currency}  нет\n")

    descriptions = transaction_descriptions(transactions)
    m = int(
        input(
            "\nвведите колличество транзакций, описание которых вы хотите увидеть: \n"
        )
    )

    try:

        for i in range(m):
            for transaction in transactions:
                description = next(descriptions)
                print(f'описание транзакции {transaction["id"]}: {description}')
    except StopIteration:
        print(f"других операций нет\n")
