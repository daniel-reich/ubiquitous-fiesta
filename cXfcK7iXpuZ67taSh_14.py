
def mystery_func(txt):
    s = ""
    for i in range(0, len(txt)-1, 2):
        s += txt[i] * int(txt[int(i+1)])
    return s

