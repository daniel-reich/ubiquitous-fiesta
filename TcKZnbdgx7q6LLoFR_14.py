
def collect(s, n):
    return [] if len(s)<n else sorted(collect(s[n:], n) + [s[:n]])

