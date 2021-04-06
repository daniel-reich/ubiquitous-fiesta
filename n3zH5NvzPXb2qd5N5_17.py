
def how_mega_is_it(n):
    n = abs(n)
    if n < 100:
        return "not a mega milestone"
    p = 1
    while 10**p <= n:
        p = p+1
    return (p-2) * 'MEGA ' + 'milestone'

