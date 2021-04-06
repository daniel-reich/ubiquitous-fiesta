
def euclidean(a, b):
  if a < b:
    c = a
    a = b
    b = c
  r = a % b
  while r != 0:
    a = b
    b = r
    r = a % b
  return b

