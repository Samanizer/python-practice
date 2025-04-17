def valid_parenthesis(s: str) -> bool:
    stack = []
    for c in s:
        if c in '({[':
            stack.append(c)
        elif c == ')':
            if stack:
                if stack.pop() != '(':
                    return False
            else:
                return False
        elif c == '}':
            if stack:
                if stack.pop() != '{':
                    return False
            else:
                return False
        elif c == ']':
            if stack:
                if stack.pop() != '[':
                    return False
            else:
                return False
    return False if stack else True
                
            