
def ordered_matrix(a, b):
  return [[y for y in range(x,x+b)] for x in range(1,(a*b)+1,b)]

