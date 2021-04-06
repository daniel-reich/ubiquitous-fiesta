
def list_operation(x, y, n):
  lst = [num for num in range(x, y+1)]
  return [i for i in lst if i % n == 0]

