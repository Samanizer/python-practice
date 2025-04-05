import heapq

def k_largest(arr, k):
    min_heap = []
    for e in arr:
        if len(min_heap) < k:
            heapq.heappush(min_heap, e)
        else:
            if e > min_heap[0]:
                heapq.heapreplace(min_heap, e)
    return min_heap[0]

if __name__ == "__main__":
    a = [2,1,8,3,7,5,0,4]
    print(k_largest(a, 2))
    
    a = sorted(a, reverse=True)
    print(a[2-1])