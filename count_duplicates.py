def count_duplicates(text):
    # 將字串轉換為小寫，以忽略大小寫差異
    text = text.lower()
    # 使用字典來記錄每個字符的出現次數
    char_count = {}
    for char in text:
        # 增加或更新字符計數
        char_count[char] = char_count.get(char, 0) + 1

    # 計算重複出現的字符數量
    duplicates = sum(1 for count in char_count.values() if count > 1)
    return duplicates
