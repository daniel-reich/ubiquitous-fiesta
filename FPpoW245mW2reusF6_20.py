
def even_last(lst):
  s = 0
  for i in range(len(lst)):
    if i % 2 == 0: s += (lst[i] * lst[-1])
  return s

