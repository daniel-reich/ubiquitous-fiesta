
def next_letters(s):
    if s == "":
        return "A"
    s = [ord(i) for i in s][::-1]
    b, r = 1, ""
    for i in range(len(s)):
        if s[i] + b == 91:
            r = "A" + r
            b = 1
        else:
            r = chr(s[i] + b) + r
            b = 0
    if b == 1:
        r = "A" + r
    return r

