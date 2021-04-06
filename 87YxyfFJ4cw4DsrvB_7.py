
def generate_rug(n):
  out = n//2
  m = []
  for j in range(n):
    row = [0]*n
    m.append(row)
  for k in range(out):
    val = out - k
    ub = k
    lb = n-k-1
    for l in range(ub, lb+1):
      m[ub][l] = val
      m[lb][l] = val
      m[l][ub] = val
      m[l][lb] = val
  return m

