
def license_plate(s, n, res=None):
    if res is None:
        s = "".join(c.upper() for c in s if c != "-")
        res = []
    return license_plate(s[:-n], n, [s[-n:]] + res) if s else "-".join(res)

