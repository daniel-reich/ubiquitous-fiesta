
def collect(s, n, ans=[]):
    if len(s) < n:
        return sorted(ans)
    return collect(s[n:], n, ans + [s[:n]])

