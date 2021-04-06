
def pilish_string(string):
    from math import pi, floor
    if not string:
        return ''
    dPi = [int(d) for d in str(floor(pi * 10 ** 14))]
    words = []
    for n in dPi:
        words.append([n, string[:n]])
        string = string[n:]
        if not string:
            break
    lastword = words[-1][1]
    lastlen = words[-1][0]
    words[-1][1] = lastword.ljust(lastlen, lastword[-1])
    return ' '.join(w[1] for w in words)

