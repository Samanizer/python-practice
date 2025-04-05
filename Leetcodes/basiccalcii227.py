def basic_calc(s: str) -> int:
    stack = []
    operator = '+'
    for e in s:
        if e.isdigit():
            if operator == '+':
                stack.append(int(e))
            elif operator == '*':
                stack.append(stack.pop() * int(e))
        elif e == '+':
            operator = '+'
        elif e == '*':
            operator = '*'
    return sum(stack)

if __name__ == "__main__":
    exp = " 3 + 4 * 2"
    print(basic_calc(exp))