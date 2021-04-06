
def second_difference(n):
  x, y, z = n[:3]
  return (z-y) - (y-x)
​
def quad_sequence(lst):
  a = second_difference(lst) / 2
  b = (lst[1] - a*(2**2)) - (lst[0] - a*(1**2))
  c = (lst[0] - a*(1**2)) - b
  y = []
  print(a, b, c)
  for i in range(len(lst)+1, len(lst)+len(lst)+1):
    r = (a*(i**2)) + (b*i) + c
    y.append(int(r))
  return y

