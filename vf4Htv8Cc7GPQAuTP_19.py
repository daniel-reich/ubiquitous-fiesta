
def list_operation(x, y, n):
  list = []
  for i in range(x, y+1):
    if i % n == 0:
      list.append(i)
  return list

