
def sort_it(lst):
  A=[]
  for x in lst:
    if type(x)==type(1):
      A.append((x, x))
    else:
      A.append((x[0],x))
  B=[y[1] for y in sorted(A)]
  return B

