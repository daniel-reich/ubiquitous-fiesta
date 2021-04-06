
def true_alphabetic(txt):
    s = ''
    for x in txt:
        if x != ' ':
            s += x
    s = sorted(s)
    ans = ''
    j = 0
    for x in txt:
        if x == ' ':
            ans += x
        else:
            ans += s[j]
            j += 1
    return ans

