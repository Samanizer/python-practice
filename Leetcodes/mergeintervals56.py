def merge_intervals(nums):
    if not nums:
        return []
    nums.sort(key=lambda x: x[0])
    result = [nums[0]]
    j = 0
    for i in range(1, len(nums)):
        if nums[i][0] <= result[j][1]:
            result[j][1] = max(result[j][1], nums[i][1])
        else:
            result.append(nums[i])
            j += 1
    
    return result 