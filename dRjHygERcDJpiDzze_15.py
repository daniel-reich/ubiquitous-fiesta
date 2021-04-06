
def lengthen(a, b):
  if len(a) < len(b):
    c,a = a,b
    b = c
  b = b*len(a)
  return b[:len(a)]

