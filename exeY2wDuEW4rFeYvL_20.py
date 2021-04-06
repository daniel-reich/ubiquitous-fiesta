
def ordered_matrix(a, b):
  x=list(range(1,a*b+1))
  return [x[i:i+b] for i in range(0,a*b,b)]

