
def license_plate(s, n):
  p, s = [], s.replace("-", "")
  while len(s): p, s = [s[-n:]] + p, s[:-n]
  return "-".join(p).upper()

