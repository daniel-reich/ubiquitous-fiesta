
vowels = "AEIOU"
consonants = ''.join([chr(i) for i in range(65, 91) if chr(i) not in vowels])
​
def is_authentic_skewer(s):
    if s[0] not in consonants or s[-1] not in consonants:
        return False
    idx = s.find('-')
    if idx < 0:
        return False
    cnt = 0
    while idx < len(s) and s[idx] == '-':
        cnt += 1
        idx += 1
    delim = '-' * cnt
    L = s.split(delim)
    for i in range(len(L)):
        c = L[i]
        if len(c) != 1:
            return False
        if i % 2 == 0:
            if c not in consonants:
                return False
        else:
            if c not in vowels:
                return False    
    return True

