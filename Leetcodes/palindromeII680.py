def is_valid(s: str) -> bool:
    def is_palindrome(sub):
        if sub == sub[::-1]:
            return True
        else:
            return False
    
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return is_palindrome(s[left:right]) or is_palindrome(s[left+1:right+1])
        else:
            left += 1
            right -= 1
    return True

if __name__ == "__main__":
    s = 'aaaaaaaaa'
    print(is_valid(s))