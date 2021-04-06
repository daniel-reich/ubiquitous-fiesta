
def jumping_frog(n, st):
  f,s = 1,0
  while s < len(st):
    j,f = st[s],f+1
    if j==0: return "no chance :-("
    s += -j if s-j>=0 and s+j<n and st[s-j]>2*st[s+j] and j!=st[s-j] else j
  return f

