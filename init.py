import fitness

if __name__ == "__main__":
    assert fitness.calculate_fitness("1000000000") == 3
    assert fitness.calculate_fitness("1100000000") == 8
    assert fitness.calculate_fitness("1110000000") == 12
    assert fitness.calculate_fitness("1111000000") == 29
    assert fitness.calculate_fitness("1111100000") == 41
    assert fitness.calculate_fitness("1111110000") == 49
    assert fitness.calculate_fitness("1111111000") == 0
