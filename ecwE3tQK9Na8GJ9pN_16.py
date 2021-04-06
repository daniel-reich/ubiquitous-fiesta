
def little_big(n):
    seq = [5, 100]
    c = 0
    d = 5
    e = 100
    while c < 14:
        d = d + 1
        e = e * 2
        seq.append(d)
        seq.append(e)
        c = c + 1
​
    return seq[n-1]

