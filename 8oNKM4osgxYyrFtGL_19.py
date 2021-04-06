
def multiply(l):
  n = []
  ll = len(l)
  for w in l:
    i = []
    ll2 = ll
    while ll2 > 0:
      i.append(w)
      ll2 = ll2 - 1
    n.append(i)
  return n

