
def collect(s, n, res=None):
    if res is None:
        res = []
    return (collect(s[n:], n, res + [s[:n]])
            if len(s) >= n else (sorted(res) if res else []))

