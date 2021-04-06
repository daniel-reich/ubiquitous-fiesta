
def list_operation(x, y, n):
  c=[]
  for i in range(x,y+1):
    if i%n==0:
      c.append(i)
  return c

