
def list_operation(x, y, n):
  lst = []
  for i in range(x,y+1):
    if i % n == 0 : lst.append(i)
  return lst

