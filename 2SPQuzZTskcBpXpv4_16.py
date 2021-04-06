
def euclidean(a, b):
  if a < b:
    c = b
    b = a
    a = c
  r = a%b
  if  r == 0:
    return b
  else:
    a = b
    b = r
    return euclidean(a,b)

