def reverse_segment(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

arr = [1, 2, 3, 4, 5, 6]
reverse_segment(arr, 2, 4)
# print(arr)

def split_equal_sum(arr):
    if sum(arr) % 2 != 0:
        return None
    half = sum(arr) // 2
    running = 0
    for i in range(len(arr)): 
        running += arr[i]
        if running == half:
            return arr[:i+1], arr[i+1:]
    

# print(split_equal_sum([2, 2, 2, 2]))  # expected: [1, 2], [3, 3]
# print(split_equal_sum([5, 1, 2, 3]))  # expected: None

