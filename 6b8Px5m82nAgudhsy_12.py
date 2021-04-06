
def next_number(num):
  n = str(num)
  R = range(len(n))
  swap = [(i1,i2) for i1 in R for i2 in R if i1<i2 and int(n[i1])<int(n[i2])]
  cands = sorted(swap,key = lambda t: (int(t[0]),-int(n[t[1]])))
  if not cands: return num
  k1, k2 = cands[-1]
  return int(n[:k1]+n[k2]+"".join(sorted(n[k1:k2]+n[k2+1:])))

