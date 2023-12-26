def abbrev_name(name):
    # 使用split()函數將名字分成單詞
    words = name.split()
    # 取得每個單詞的首字母並轉換為大寫，然後用句點"."連接起來
    return f"{words[0][0].upper()}.{words[1][0].upper()}"
