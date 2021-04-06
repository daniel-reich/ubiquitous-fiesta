
def junction_or_self(n):
    res = [i for i in range(max(n - 27, 1),n) if n == i + sum(int(k) for k in str(i))]
    return list(reversed(res)) if res!=[] else "Self"

