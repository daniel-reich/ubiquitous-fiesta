
def arithmetic_progression(start, diff, n):
  lst, c = [], start
  while len(lst) < n:
    lst.append(c)
    c += diff
  return ', '.join(map(str, lst))

