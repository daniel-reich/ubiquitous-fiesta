
def euclidean(a, b):
  if a < b:
    x = a
    a = b
    b = x
  r = a%b
  if r == 0:
    return b
  return euclidean(b,r)

