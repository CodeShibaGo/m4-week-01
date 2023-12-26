def unique_in_order(iterable):
    result = []
    prev_char = None

    for char in iterable:
        if char != prev_char:
            result.append(char)
            prev_char = char

    return result