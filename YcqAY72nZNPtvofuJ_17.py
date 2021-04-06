
def quad_sequence(lst):
  n1,n2,n3 = lst[0], lst[1], lst[2]
  a = (n1 + n3 - 2 * n2)/2
  b = n3 - a - n2
  return [int(a * i**2 + b * i + n2) for i in range(len(lst)-1, 2*len(lst)-1)]

