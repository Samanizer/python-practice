import math

# def CreateMap(s):
#     m = {}
#     for i, c in enumerate(s):
#         m[c] = i
#     print (m)

# s = "dkfhkdahfkjhdafkhdkfjh;9ieuoruew"

# CreateMap(s)


# Two Pointers Sample
# Check if its a Palindrome
print("================Palindrome==============")
def isPalindrome(s):
    p1 = 0
    p2 = len(s) - 1

    for i in range(len(s) // 2):
        if s[p1] != s[p2]:
            return False
        if p1 == p2 or p2 - p1 == 1:
            return True
        p1 += 1
        p2 -= 1
    return True #never reaches
s = "abcba"
print(isPalindrome(s))
s = "aaa"
print(isPalindrome(s))
s = "aabbca"
print(isPalindrome(s))

# Sliding Window
# Max Sum of Subarray of k length
print("================MaxSum Subarray==============")
arr = [1,4,8,4,2,9,4,6,2,9]
k = 3

def MaxSum(arr, k):
    start = 0
    end = 2
    win_sum = sum(arr[:k])
    max_sum = win_sum
    for i in range(k, len(arr)):
        win_sum += arr[i] - arr[i-k]
        if win_sum > max_sum:
            max_sum = win_sum
    return max_sum

print(MaxSum(arr, k))

print(sum([25, 25, 25, 25, 26, 28, 83]))

ar2 = [1,2,3,4,5,6,7,8,9,10]
ar3 = [ele * 2 for ele in ar2]

print("Sum", sum(ar3))
while ar3:
    print(ar3.pop())
