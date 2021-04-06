
def decrypt(s):
    ans = ""
    while len(s) >= 3:
        if s[2] == '#':
            ans += chr(96 + int(s[:2]))
            s = s[3:]
        else:
            ans += chr(96 + int(s[0]))
            s = s[1:]
    for c in s:
        ans += chr(96 + int(c))
    return ans

