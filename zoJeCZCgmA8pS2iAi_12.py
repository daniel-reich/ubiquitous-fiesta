
def func_sort(lst):
  depth = lambda f: (1 + depth(f())) if isinstance(f,type(lambda: 1)) else 0
  return sorted(lst, key = depth)

