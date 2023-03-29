from fitness import calculate_fitness

if __name__ == "__main__":

    # Check values and answers
    FITNESS_TEST_VALUES = [
        [1, 0, 1, 1, 0, 1, 0, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 1, 0, 1, 1, 0, 0],
        [0, 1, 1, 0, 0, 0, 1, 1, 0, 1],
        [0, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    ]

    # Correct values
    FITNESS_CHECK_VALUES = [48, 53, 26, 30, 29, 65, 20, 42, 23, 49]

    for index, backpack in enumerate(FITNESS_TEST_VALUES):
        assert (
            calculate_fitness(FITNESS_TEST_VALUES, index) == FITNESS_CHECK_VALUES[index]
        ), f"Expected value: {FITNESS_CHECK_VALUES[index]}, got instead: {calculate_fitness(FITNESS_TEST_VALUES, index)}"
