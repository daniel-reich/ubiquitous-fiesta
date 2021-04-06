
def pos_neg_sort(lst):
  pi = []
  p = []
  for i in range(len(lst)):
    if lst[i] > 0:
      pi.append(i)
      p.append(lst[i])
  p = sorted(p)
  a = 0
  for i in range(len(lst)):
    if i in pi:
      lst[i] = p[a]
      a += 1
  return lst

