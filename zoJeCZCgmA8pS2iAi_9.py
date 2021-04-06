
def func_sort(lst):
  depth = lambda x: 1 + depth(x()) if callable(x) else 0
  return sorted(lst, key=depth)

