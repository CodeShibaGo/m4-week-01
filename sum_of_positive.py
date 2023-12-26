def positive_sum(arr):
    # 初始化總和為0
    total = 0
    # 遍歷列表中的每個數字
    for num in arr:
        # 如果數字大於0，將其加到總和中
        if num > 0:
            total += num
    return total
