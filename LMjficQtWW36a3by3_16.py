
def probability(lst, n):
  z=0
  for i in lst:
    if n<=i:
      z = z+1
  q = (z/(len(lst))*100)
  return round(q,1)

