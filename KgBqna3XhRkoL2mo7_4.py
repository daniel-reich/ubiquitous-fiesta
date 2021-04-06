
letters = {str(i - 96): chr(i) for i in range(97, 123)}
def decrypt(s):
    len_s = len(s)
    i = 0
    res = []
    while i < len_s:
        if i + 2 < len_s and s[i + 2] == "#":
            res.append(letters[s[i: i + 2]])
            i += 3
        else:
            res.append(letters[s[i: i + 1]])
            i += 1
    return "".join(res)

