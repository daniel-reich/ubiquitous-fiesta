
def nearest_element(n, lst):
  l1 = [abs(n-lst[i]) for i in range(len(lst))]
  m = min(l1)
  n1 = l1.index(m)
  if l1.count(m) > 1:
    n2 = l1[n1+1:].index(m) + n1 + 1
    if lst[n1] > lst[n2]:
      return n1
    else:
      return n2
  else:
    return n1

