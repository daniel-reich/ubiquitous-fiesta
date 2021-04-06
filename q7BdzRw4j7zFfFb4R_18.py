
def merge_arrays(a, b):
  values = []
  i = 0
  length = max(len(a), len(b))
  while i <= length:
    try:
      values.append(a[i])
    except IndexError:
      pass
    try:
      values.append(b[i])
    except IndexError:
      pass
    i += 1
  return values

