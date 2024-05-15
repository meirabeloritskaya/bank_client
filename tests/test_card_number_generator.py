from src.generators import card_number_generator


def test_card_number_generator():

    expected_resulted = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]

    resulted = [card_number for card_number in card_number_generator(1, 5)]
    assert resulted == expected_resulted
