def calculate_average(nums):
    if not nums:
        return 0
    total = sum(nums)
    return total / len(nums)
