
def collect(s, n):
    if n > len(s):
        return []
    d = [s[i:i + n] for i in range(0, len(s), n) if len(s[i:i + n])==n]
    return sorted(d)

