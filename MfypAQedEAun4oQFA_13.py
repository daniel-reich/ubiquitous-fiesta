
def perrin(n):
  p = [3, 0, 2]
  print(n)
  for i in range(3, n+1):
    print(i, p)
    p.append(p[i-2]+p[i-3])
  return p[n]

