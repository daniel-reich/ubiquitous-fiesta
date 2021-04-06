
def mult_table(n):
  a = []
  for i in range(1,n+1):
    b = []
    for j in range(1,n+1):
      b.append((j*i))
    a.append(b)
  return a

