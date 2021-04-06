
def multiplication_table(n):
  a=[]
  for i in range(1,n+1):
    x,b=i,[]
    for j in range(1,n+1):
      b.append(i)
      i+=x
    a.append(b)
  return a

