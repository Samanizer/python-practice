def contin_sum(nums, k):
    if k == 0:
        for i in range(len(nums) - 1):
            if nums[i] == 0 and nums[i+1] == 0:
                return True
        return False
    
    mod_map = {0: -1}
    curr_sum = 0
    
    for i, num in enumerate(nums):
        curr_sum += num
        mod = curr_sum % k
        
        if mod in mod_map and i - mod_map[mod] >= 2:
            return True
        if mod not in mod_map:
            mod_map[mod] = i
    
    return False