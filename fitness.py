import utils


def calculate_fitness(backpack: str):
    """
    :param backpack: String of 0 and 1, total length 10
    :return: Total weight and price of items in backpack
    """
    weight = 0
    price = 0
    for count, item in enumerate(backpack, start=1):
        if item == '1':
            weight += utils.INPUT_DATA_DICT.get(count).weight
            price += utils.INPUT_DATA_DICT.get(count).price

    if weight > utils.MAX_WEIGHT:
        return 0
    else:
        return price
