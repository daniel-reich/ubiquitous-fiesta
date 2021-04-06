
def doubleton(n):
  x = n + 1
  while len(set([i for i in str(x)])) != 2:
    x += 1
  return x

