def maxones(nums, k):
    left = 0
    zeroes = 0
    max_ones = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeroes += 1
        if zeroes > k:      # or while zeroes > k
            while nums[left] != 0:
                left += 1
            zeroes -= 1
        max_ones = max(max_ones, right - left + 1)
    return max_ones