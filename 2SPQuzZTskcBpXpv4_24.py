
def euclidean(a, b):
  if a<b:
    b = a
    a = b
  r = a%b   
  while r != 0:
    a = b
    b = r
    r = a%b
  return b

