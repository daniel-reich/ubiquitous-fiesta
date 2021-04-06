
def merge_arrays(a, b):
  lst = [i for _tup in zip(a, b) for i in _tup]
  return lst if len(a) == len(b) else lst + a[len(b):] if len(a) > len(b) else lst + b[len(a):]

