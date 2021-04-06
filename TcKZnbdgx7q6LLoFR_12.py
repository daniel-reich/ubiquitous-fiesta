
def collect(s, n, res=[]):
    if len(s) < n:
        return sorted(res)
    return collect(s[n:], n, res + [s[:n]])

