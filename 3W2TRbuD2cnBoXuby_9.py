
def collect(s, n):
  return sorted([s[i:i+n] for i in range(0,len(s)-n+1,n)])

