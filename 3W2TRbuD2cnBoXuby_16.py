
def collect(s, n):
  return sorted([b for b in [s[a:a+n] for a in range(0,len(s),n)] if len(b)==n])

