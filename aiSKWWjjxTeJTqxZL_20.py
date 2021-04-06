
def complete_square(lst):
  l1 = []
  m = len(lst)
  n = len(lst[0])
  if m > n:
    l = m - n
    for row in lst:
      r = row
      for i in range(l):
        r.append(0)
      l1.append(r)
    return l1
  elif m < n:
    l = n - m
    l1 = lst
    r = [0 for i in range(n)]
    for i in range(l):
      l1.append(r)
    return l1
    
  else:
    return lst

