
def max_total(n):
  a=[]
  for i in range(5):
    a.append(max(n))
    n.remove(max(n))
  return sum(a)

