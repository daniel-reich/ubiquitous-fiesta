
def multiplication_table(n):
  l1=[]
  for i in range(1, n+1):
    l2=[]
    for j in range(1, n+1):
      l2.append(i*j)
    l1.append(l2)
  return l1

