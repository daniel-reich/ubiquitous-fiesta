
def zero_indices(lst, k):
  from itertools import combinations as co
  l = list(co([i for i in range(len(lst)) if lst[i] == 0], k))
  v = []
  for i in l:
    lst1 = lst[:]
    for j in i:
      lst1[j] = 1
    u = max([len(v) for v in ''.join([str(k) for k in lst1]).split('0')])
    v.append((-u, i))
  v = sorted(v)
  return list(v[0][1])

