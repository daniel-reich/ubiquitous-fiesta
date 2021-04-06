
def numberSequence(n, s = 1, r = None, t = None):
    if not t:
        if n < 3 : return "1" + " 1"*(n == 2) if n > 0 else "-1"
        n, r = int(-1 * (n / 2) // 1 * -1), (n - 1) % 2; t = n
    if s:
        return " "*(t!=n)+str(n)+numberSequence(n - 1, s, r, t) if n > 1 else " 1"*(1+r) + numberSequence(n + 1, 0, r, t)
    else:
        return " "+str(n)+numberSequence(n + 1, s, r, t) if n <= t else ""

