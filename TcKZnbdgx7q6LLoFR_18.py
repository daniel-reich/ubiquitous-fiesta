
def collect(s, n):
    if len(s) < n:
        return []
    if len(s) == n:
        return [s]
    else:
        return sorted([s[0:n]] + collect(s[n:], n))

