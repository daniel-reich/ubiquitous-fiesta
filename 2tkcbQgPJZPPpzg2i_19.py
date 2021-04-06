
def sum_of_holes(N):
  return sum([get_holes(i) for i in range(1, N+1)])
  
def get_holes(n):
  h = 0
  for i in str(n):
    if i in ('4', '6', '9', '0'):
      h += 1
    if i == '8':
      h += 2
  return h

