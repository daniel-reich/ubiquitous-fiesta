
def collect(s, n, meh = None):
  if not meh:
    meh = []
  if len(s)<n:
    return sorted(meh)
  meh.append(s[:n])
  return collect(s[n:], n, meh)

