
def lcm(n1, n2):
  a = []
  x = [n1, n2]
  y = max(x)
  z = min(x)
  for x in range(y, y*z+1, y):
    print(x)
    if x % n1 == 0 and x % n2 == 0:
      a.append(x)
  print(a)
  return a[0]

