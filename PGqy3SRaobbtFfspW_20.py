
def simple_pair(lst, n):
  for i in lst:
    if i and not n%i:
      l=lst.copy()
      l.pop(l.index(i))
      for j in l:
        if i*j==n:
          return [i,j]
  return None

