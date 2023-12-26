def disemvowel(s):
    # 創建一個空字串，用來存儲結果
    result = ""

    # 遍歷輸入字串的每個字元
    for char in s:
        # 如果字元不是母音，則將其添加到結果中
        if char.lower() not in "aeiou":
            result += char

    # 返回結果
    return result
