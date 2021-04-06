
def collect(s, n, lst=None):
    if not lst:
        lst = []
    if len(s) < n:
        return sorted(lst)
    lst.append(s[:n])
    collect(s[n:], n, lst)
    return sorted(lst)

