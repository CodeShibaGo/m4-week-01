def nb_dig(n, d):
    count = 0
    for i in range(n + 1):
        count += str(i).count(str(d))
    return count