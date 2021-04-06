
def merge_arrays(a, b):
  a.reverse()
  b.reverse()
  r = []
  while a+b:
    if a: r.append(a.pop())
    if b: r.append(b.pop())
  return r

