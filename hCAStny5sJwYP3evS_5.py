
def is_early_bird(_range, n):
  k = 0
  seq, sn = '', str(n)
  early, ind = [], [[-1]]
  
  for i in range(_range + 1):
    s = str(i)
    seq += s
    k = seq.find(sn, k)
    if k != -1:
      if not early and i < n:
        early.append('Early Bird!')
      ind.append(list(range(k, k + len(sn))))
    k = max(0, ind[-1][0] + 1)
  return ind[1:] + early

