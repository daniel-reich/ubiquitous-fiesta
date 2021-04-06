
def find_difference(a, b):
  aa=1
  bb=1
  for i in a:
    aa*=i
  for i in b:
    bb*=i
  return abs(aa-bb)

