
def invert(s, ans=""):
    if len(s) == 0:
        return ans
    c = s[-1]
    ans += c.lower() if c <= 'Z' else c.upper()
    return invert(s[:-1], ans)

