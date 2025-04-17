
'''
You're given an array of positive integers.
Return True if there's an index i where the sum of elements 
on the left equals the sum on the right (excluding the index itself). 
Otherwise, return False.
'''

arr = [1, 1, 1, 2, 1]

def bal_array(arr):
    for i in range(1, len(arr)-1):
        sum1 = sum(arr[:i])
        sum2 = sum(arr[i:])
        if sum1 == sum2:
            return True
    return False

def bal_array2(arr):
    total = sum(arr)
    left_sum = 0
    for i in range(len(arr) - 1):
        left_sum += arr[i]
        if left_sum == total - left_sum:
            return True
    return False
    