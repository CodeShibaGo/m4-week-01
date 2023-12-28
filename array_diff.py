def array_diff(a, b):
    # 創建一個新數組來存儲結果
    result = []
    # 遍歷數組 a 中的每個元素
    for item in a:
        # 如果元素不在數組 b 中，則添加到結果數組中
        if item not in b:
            result.append(item)
    return result