
def tower_of_hanoi(n, m):
    def counter(a, b):
        nonlocal m
        m -= 1
        res[b].append(res[a].pop())
        return m==0
​
    def tow(a, b, dsk):
        if dsk:
            c = 3 - a - b
            return tow(a,c, dsk-1) or counter(a, b) or tow(c,b, dsk-1)
​
    res = list(range(n,0,-1)), [], []
    tow(0, 2, n)
    return res

