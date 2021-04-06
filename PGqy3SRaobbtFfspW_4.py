
def simple_pair(lst, n):
  for i in range(len(lst)):
    for a in lst[i + 1:]:
      if lst[i] * a == n:
        return [lst[i], a]

