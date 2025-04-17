'''
Given an array of integers, and two indices L and R (inclusive), 
reverse the elements between L and R in-place.
'''
arr = [1, 2, 3, 4, 5, 6]
L = 2
R = 5

def reverse_sa(arr, l, r):
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1