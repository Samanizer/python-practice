def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2
    left =  merge_sort(lst[:mid])
    right =  merge_sort(lst[mid:])
    
    merged = merge(left, right)
    
    return merged
    

def merge(left, right):
    i, j = 0, 0
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
    elif j < len(right):
        result += right[j:]
    
    return result

print(merge_sort([38, 27, 43, 3, 9, 82, 10]))