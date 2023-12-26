def century(year):
    # 如果年份是整百年，則它屬於該年代的世紀
    if year % 100 == 0:
        return year // 100
    # 否則，它屬於下一個世紀
    return year // 100 + 1
