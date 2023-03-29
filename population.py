import numpy as np
from utils import CHROMOSOME_COUNT


def generate_population(
    population_size: int, chromosome_count=CHROMOSOME_COUNT
) -> list:
    """
    :param population size: value to define population size
    :param chromosom_count: value to define size of each chromosome (element of the list)
    :return: list of (chromosome * chromosome count) * population size
    """
    return np.random.randint(low=0, high=2, size=(population_size, chromosome_count))
