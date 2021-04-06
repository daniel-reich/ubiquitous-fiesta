
def increment_string(txt):
    n = ""
    while len(txt) > 0 and '0' <= txt[-1] <= '9':
        n = txt[-1] + n
        txt = txt[:-1]
    if n == "":
        return txt + '1'
    L = len(n)
    n = str(int(n) + 1).zfill(L)
    return txt + n

