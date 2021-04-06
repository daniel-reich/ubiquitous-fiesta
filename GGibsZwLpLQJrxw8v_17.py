
def get_lucky_number(size, nth):
    s = [i for i in range(1, size + 1)]
    sl = len(s)
    k = 1
    d = 2
    r = []
    sf = 1
    while d < sl:
        for i in range(sf, sl, d):
            if i != 0 and i != -1:
                s[i] = '-'
        r = [i for i in s if i != '-']
​
        if k <= len(r):
            d = r[k]
        else:
            break
        k += 1
        s = r
        sl = len(s)
        sf = -1
​
    return r[nth-1]

