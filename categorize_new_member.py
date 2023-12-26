# 定義函數 categorize_new_member
def categorize_new_member(data):
    # 初始化一個空列表，用於存儲成員的分類結果
    result = []
    # 遍歷每位成員的資料
    for age, score in data:
        # 根據條件判斷成員類別
        if age >= 55 and score > 7:
            result.append("Senior")
        else:
            result.append("Open")
    # 返回分類結果列表
    return result