
def func(lst):
  if type(lst)!=list: return 0
  return len(lst) + sum(func(e) for e in lst)

