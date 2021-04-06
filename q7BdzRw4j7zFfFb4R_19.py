
def merge_arrays(a, b):
  a, b, ret = a[::-1], b[::-1], []
  for x in range(max(len(a), len(b))):
    if a:
      ret.append(a.pop())
    if b:
      ret.append(b.pop())
  return ret

