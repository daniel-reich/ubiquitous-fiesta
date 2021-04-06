
def digit_count(n):
  d, c, n = dict(), dict(), list(str(n))
  for i, k in enumerate(n):
    d[k], c[k] = d[k]+[i] if k in d else [i], n.count(k)
  for k in d.keys():
    for i in d[k]: n[i] = c[k]
  return int(''.join(map(str, n)))

