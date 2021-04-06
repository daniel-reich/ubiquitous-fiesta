
def license_plate(s, n):
    s = s.upper().replace("-","")
    res = []
    while len(s) >= n:
      res.append(s[-n:])
      s = s[:-n]
    if len(s) > 0:
      res.append(s)
    return "-".join(res[::-1])

