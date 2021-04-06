
def func_sort(lst):
  key = lambda f: 0 if not callable(f) else 1 + key(f())
  return sorted(lst, key = key)

