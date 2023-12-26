def find_smallest_int(arr):
    # 初始化最小值為陣列的第一個元素
    smallest = arr[0]
    # 遍歷陣列中的每個元素
    for num in arr:
        # 如果目前的數字比最小值小，更新最小值
        if num < smallest:
            smallest = num
    return smallest
