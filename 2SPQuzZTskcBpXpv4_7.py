
def euclidean(a, b):
  count = 0
  while count != 1:
    c = 1
    if a < b:
      c = a
      a = b 
      b = c
    r = a%b
    if r == 0:
      count = 1
      return b
    a = b
    b = r

