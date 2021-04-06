
def list_operation(x, y, n):
  foo = []
  for i in range(x, y+1):
    if i % n == 0:
      foo.append(i)
  return foo

