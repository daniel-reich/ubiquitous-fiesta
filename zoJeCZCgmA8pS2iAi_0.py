
def func_sort(lst):
  f = lambda g, n=0: f(g(), n+1) if callable(g) else n
  return sorted(lst, key=f)

