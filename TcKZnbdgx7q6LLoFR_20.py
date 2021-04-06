
def collect(s, n):
    if len(s) < n:
        return []
    else:
        return sorted([s[0:n]] + collect(s[n:],n))

