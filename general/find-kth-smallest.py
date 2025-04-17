'''
Find the kth smallest element in an array
'''
import heapq

def k_smallest(nums, k):
    heap = []
    for n in nums:
        heapq.heappush(heap, -n)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return -heap[0]

nums = [1,2,3,4,5,6]
k = 3
print(k_smallest(nums, k))