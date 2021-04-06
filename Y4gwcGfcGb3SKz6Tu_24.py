
def max_separator(txt):
    long = 0
    ans = []
    for o in range(97, 123):
        sep = chr(o)
        if txt.count(sep) >= 2:
            txt2 = txt[txt.index(sep):]
            while txt2[-1] != sep:
                txt2 = txt2[:-1]
            l = max([len(_) for _ in txt2.split(sep)])
            if l > long:
                ans = [sep]
                long = l
            elif l == long:
                ans.append(sep)
    return ans

