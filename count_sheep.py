def count_sheep(sheep):
    count = 0
    for is_sleeping in sheep:
        if is_sleeping:
            count += 1
    return count
