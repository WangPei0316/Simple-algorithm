def twoSum(nums, target):
    """
    nums为传入的列表
    target为求和之数
    """
    new_nums = [(v, i) for i, v in enumerate(nums)]
    new_nums_sorted = sorted(new_nums, key=lambda x: x[0])
    l, r = 0, len(nums) - 1
    while l < r:
        if new_nums_sorted[l][0] + new_nums_sorted[r][0] == target:
            return [new_nums_sorted[l][1], new_nums_sorted[r][1]]
        elif new_nums_sorted[l][0] + new_nums_sorted[r][0] > target:
            r -= 1
        else:
            l += 1


print(twoSum([1, 3, 6, 7, 8], 13))
