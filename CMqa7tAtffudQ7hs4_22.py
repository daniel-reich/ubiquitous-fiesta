
def sorting_steps(lst):
  l = len(lst)
  if l < 2:
    return []
  M = max(lst)
  i = lst.index(M)
  if i == l-1:
    return sorting_steps(lst[:-1])
  return [(i,l-1)] + sorting_steps(lst[:i]+[lst[-1]]+lst[i+1:-1])

