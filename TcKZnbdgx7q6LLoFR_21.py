
def collect(s, n, final=[]):
  if s in str_vector:
    final = []
  if len(s) >= n:
    final.append(s[:n])
    a=s[n:]
    return collect(a,n,final)
  else:
    return sorted(final)

