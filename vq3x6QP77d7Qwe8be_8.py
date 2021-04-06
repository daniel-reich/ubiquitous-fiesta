
def odd_square_patch(lst):
  n = len(lst)
  m = len(lst[0])
  d = {(i,j):0 for i in range(n) for j in range(m) if lst[i][j]%2}
  for i,j in d.keys():
    for k in range(1,min(n,m)+1):
      if all((i+r,j+s) in d.keys() for r in range(k) for s in range(k)):
        d[i,j]+=1
  return max(d.values()) if d else 0

