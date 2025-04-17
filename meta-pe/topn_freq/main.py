'''
Given a list of integers, return the top N most frequent elements.
If multiple numbers have the same frequency, return the one with lower value first.
'''

from collections import Counter

arr = [1, 1, 2, 2, 3, 3, 3, 4]
n = 2

def topn(arr, n):
    counter = Counter(arr)
    
    sorted_list = sorted(
        counter.items(),
        key=lambda x: (-x[1], x[0])
    )
    return [num for num, _ in sorted_list[:n]]
    