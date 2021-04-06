
def collect(s, n):
  return sorted([s[n*i:n*i+n] for i in range(len(s)//n)])

