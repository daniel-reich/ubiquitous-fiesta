
def simple_pair(lst, n):
  for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
      x = lst[i]
      y = lst[j]
      if x * y == n:
        return [x, y]
  return None

