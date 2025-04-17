def is_palindrome(s: str) -> bool:
    s = s.strip()
    s = s.lower()
    ls = list(s)
    for i, c in enumerate(ls):
        if not c.isalpha():
                ls[i] = ''
    s = ''.join(ls)
    return s == s[::-1]

def is_palindrome2(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

s = "A man, a plan, a canal: Panama"

print(is_palindrome(s))
print(is_palindrome2(s))