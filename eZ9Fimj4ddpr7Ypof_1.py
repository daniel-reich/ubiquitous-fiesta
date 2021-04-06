
def mumbling(s):
    res = "";
    for i in range(len(s)):
        res += s[i].upper() + s[i].lower() * i + "-"
    return res[:-1]

