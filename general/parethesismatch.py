import string

def ParenthesisMatcher(s: string):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            print(stack)
            if not stack:
                return False
            else:
                stack.pop()
    print(stack)
    return False if stack else True
            




if __name__ == "__main__":
    s = "(((())(()"
    print(ParenthesisMatcher(s))
    s = "(((())))(())()"
    print(ParenthesisMatcher(s))
    s = ""
    print(ParenthesisMatcher(s))
    s = "ab(c)d((a)bc)"
    print(ParenthesisMatcher(s))
    