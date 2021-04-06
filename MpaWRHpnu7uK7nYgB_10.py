
def doubleton(n):
  n = n + 1
  while len(set(str(n))) != 2:
    n += 1
  return n

