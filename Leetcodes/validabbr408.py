def is_valid_abbr(word, abbr):
    i, j = 0, 0
    while i < len(word) and j < len(abbr):
        if abbr[j].isalpha():
            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue
            else:
                return False
        elif abbr[j].isdigit():
            if abbr[j] == '0':
                return False
            else:
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                i += num
    return i == len(word) and j == len(abbr)

if __name__ == "__main__":
    w = "brokentimes"
    a = "b10"
    print(is_valid_abbr(w, a))
            
