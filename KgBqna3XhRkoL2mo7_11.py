
def decrypt(s):
    r = ""
    a  = "_abcdefghijklmnopqrstuvwxyz"
    while len(s) > 0:
        if "#" in s and s[2] == "#":
            r += a[int(s[:2])]
            s = s[3:]
        else:
            r += a[int(s[0])]
            s = s[1:]
    return r

