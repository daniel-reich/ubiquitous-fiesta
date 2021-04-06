
def title_to_number(s):
    r = 0
    s = s[::-1]
    for i in range(len(s)):
        if i == 0:
            r += (ord(s[0]) - 64)
        else:
            r += (ord(s[i]) - 64) * 26**i
    return r

