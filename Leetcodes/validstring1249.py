def validstring(s: str) -> str:
    stack = []
    result = []
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
            result.append(c)
        elif c == ')':
            if stack:
                stack.pop()
                result.append(c)
            else:
                result.append('')
                continue
        else:
            result.append(c)
    
    while stack:
        result[stack.pop()] = ''
    
    return ''.join(result)