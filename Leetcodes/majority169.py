def majority(nums):
    count = 0
    candidate = -1
    
    for num in nums:
        if count == 0:
            candidate = num
        if candidate == num:
            count += 1
        else:
            count -= 1
    
    return candidate

n = [1,2,2,2,2,2,1,1,1]
print(majority(n))