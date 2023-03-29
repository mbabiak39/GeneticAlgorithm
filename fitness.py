import utils
import population


def calculate_fitness(backpack: list, backpack_indx: int):
    """
    :param backpack: array of 1 and 0.
    :return: Total weight and price of items in backpack
    """
    weight = 0
    price = 0
    for count, item in enumerate(list(backpack[backpack_indx])):
        if int(item) == 1:
            weight += utils.INPUT_DATA_DICT.get(count).weight
            price += utils.INPUT_DATA_DICT.get(count).price

    if weight > utils.MAX_WEIGHT:
        return 0
    else:
        return price
