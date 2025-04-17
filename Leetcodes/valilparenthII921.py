def valid_parenthII(s: str) -> bool:
    open_needed = 0
    insertions = 0
    for c in s:
        if c == '(':
            open_needed += 1
        else:
            if open_needed > 0:
                open_needed -= 1
            else:
                insertions += 1
    
    return open_needed + insertions