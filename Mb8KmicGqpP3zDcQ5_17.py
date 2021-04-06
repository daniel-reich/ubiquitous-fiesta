
def josephus(n, i):
    ll = [i + 1 for i in range(n)]
    ind = 0
    inc = i-1
    while len(ll) > 1:
        ind = (ind + inc) % len(ll)
        ll.pop(ind)
        ind %= len(ll)
        inc = i - 1
    return ll[0]

