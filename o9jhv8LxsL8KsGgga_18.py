
def bound_sort(lst, bounds):
  a = lst[bounds[0]:bounds[1]+1]
  b = lst[bounds[1]+1:]
  a = sorted(a)
  c = a+b
  if c == sorted(lst):
    return True
  else:
    return False

