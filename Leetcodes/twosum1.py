def two_sum(nums, target):
    c_map = {}
    for i, num in enumerate(nums):
        if target - num in c_map:
            return [c_map[target - num], i]
        else:
            c_map[num] = i