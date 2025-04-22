def validwordabbr(word: str, abbr: str) -> bool:
    widx = 0
    num = 0
    i = 0
    while i < len(abbr):
        if abbr[i].isalpha():
            if widx < len(word) and word[widx] == abbr[i]:
                widx += 1
                i += 1
                continue
            else:
                return False
        elif abbr[i].isdigit():
            if abbr[i] == '0':
                return False
            else:
                num = 0
                n = ''
                while abbr[i].isdigit():
                    n += abbr[i]
                    i += 1
                num = int(n)
                widx += num
        if widx > len(word):
            return False
    
    return widx == len(word)
        
                