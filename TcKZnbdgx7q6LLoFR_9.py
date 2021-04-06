
def collect(s, n, r=[]):
    if len(s) < n:
        b = r.copy()
        r.clear()
        return sorted(b)
    else:
        r.append(s[: n])
        return collect(s[n:], n, r)

