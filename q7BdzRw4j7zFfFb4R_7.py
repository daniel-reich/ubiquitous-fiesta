
def merge_arrays(a, b):
  li = list(sum(zip(a, b), ()))
  mi = min(len(a), len(b))
  if len(a) > len(b):
    del a[:mi]
    li.extend(a)
  elif len(a) < len(b):
    del b[:mi]
    li.extend(b)
  return li

