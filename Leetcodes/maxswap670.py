def maxswap(num):
    lst = list(str(num))
    idx_map = {}
    for i, d in enumerate(lst):
        idx_map[d] = i
        
    for i, d in enumerate(lst):
        for x in range(9, int(d), -1):
            if str(x) in idx_map and idx_map[str(x)] > i:
                lst[i], lst[idx_map[str(x)]] = lst[idx_map[str(x)]], lst[i] 
                return int(''.join(lst))
    
    return num
