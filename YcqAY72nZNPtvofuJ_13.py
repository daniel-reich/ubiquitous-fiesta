
def quad_sequence(lst):
  l = len(lst)
  j = [lst[x+1]-lst[x] for x in range(2)]
  a = (j[1]-j[0])/2
  b = j[0]-3*a
  c = lst[0] - a - b
  return ([int(a*n**2 + b*n + c) for n in range(l+1, 2*l+1)])

