def count_duplicates(s):
    # 將字串轉為小寫，並初始化一個字典來記錄字符出現次數
    s = s.lower()
    char_count = {}

    # 遍歷字串中的每個字符
    for char in s:
        # 如果是字母字符，則更新字典中的計數
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    # 計算重複字符的數量，即字典中值大於1的鍵的數量
    duplicates_count = sum(1 for count in char_count.values() if count > 1)

    return duplicates_count
