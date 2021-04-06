
def list_operation(x, y, n):
  total=[]
  for i in range(x, y+1):
    if i % n == 0:
      total.append(i)
  return total

