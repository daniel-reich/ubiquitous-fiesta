
def multiplication_table(n):
  x = []
  for i in range(1,n+1):
    x.append([i*j for j in range(1,n+1)])
  return x

