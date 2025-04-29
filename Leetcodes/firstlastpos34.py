def firstlastpos(nums, target):
    left = 0
    right = len(nums) - 1
    
    left_idx = -1
    right_idx = -1
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] == target:
            left_idx = mid
            right = mid
        elif nums[mid] > target:
            right = mid
        else:
            left = mid + 1
    
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (right + left) // 2 + 1
        if nums[mid] == target:
            right_idx = mid
            left = mid
        elif nums[mid] > target:
            right = mid
        else:
            left = mid + 1
    
    return [left_idx, right_idx]