def find_capitals(word):
    result = ""
    for char in word:
        if char.isupper():
            result += char
    return result
