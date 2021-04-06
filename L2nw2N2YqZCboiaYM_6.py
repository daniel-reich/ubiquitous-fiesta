
def repeated(s):
    len_s = len(s)
    if len_s > 1:
        if len(set(s)) == 1:
            return True
        for i in range(2, len_s // 2 + 1):
            if not len_s % i:
                len_sub = len_s // i
                set_subs = set(s[j * len_sub: (j + 1) * len_sub]
                               for j in range(i))
                if len(set_subs) == 1:
                    return True
    return False

