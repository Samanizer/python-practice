def permulations(lst):
    if len(lst) <= 1:
        return [lst]
    
    result = []
    for i in range(len(lst)):
        el = lst[i]
        rest = lst[:i] + lst[i+1:]
        
        for perm in permulations(rest):
            result.append([el] + perm)
            
    return result

print(permulations([1,2,3,4]))