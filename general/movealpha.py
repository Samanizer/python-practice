# ch = 'a'
# print("ord a", ord(ch))
# print("ord z", ord('z'))
# ch = str(chr(ord('b') + 26 - ord('a')))

# print(ch)

def shift_right(a):
    result = []
    for c in a:
        result.append(chr((ord(c) - ord('a') + 1 % 26) + ord('a')))
    return ''.join(result)

print(shift_right('def'))