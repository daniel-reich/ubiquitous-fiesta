
def perrin(n):
  p = [3,0,2]
  while n>len(p)-1:
    p.append(sum(p[-3:-1]))
  return p[n]

