def validpalindrome(s: str) -> bool:
    def ispalindrome(sub: str) -> bool:
        return sub == sub[::-1]
    
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            if ispalindrome(s[left:right]) or ispalindrome(s[left+1:right+1]):
                return True
            else:
                return False
        left += 1
        right -= 1
    
    return True
    