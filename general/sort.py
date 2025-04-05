def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    sorted_l = merge_sort(left_half)
    sorted_r = merge_sort(right_half)
    return merge(sorted_l, sorted_r)

def merge(left, right) -> list[int]:
    i = j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < len(left):
        result += left[i:]
    if j < len(right):
        result += right[j:]
    return result

if __name__ == "__main__":
    a = [3,6,1,9,3,7,5,1]
    print(merge_sort(a))