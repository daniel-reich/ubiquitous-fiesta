
def negative_sum(s):
    tot = 0
    beg = 0
    ln = len(s)
    while True:
        try:
            i = s.index('-', beg)
            n = s[i]
            for x in s[i+1:]:
                if x.isdigit():
                    n += x
                else:
                    break
            tot += int(n)
            beg = i + 1
        except:
            break
    return tot

