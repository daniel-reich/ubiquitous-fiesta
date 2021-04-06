
def nPr(n, r):
  #n!/(n-r)!
  p = 1
  for v in range(n, n-r, -1):
    p *= v
  return p
​
def nCr(n, r):
  #n!/(r!(n-r)!)
  r = min(r, n - r)
  num = nPr(n, r)
  dnm = 1
  for i in range(2, r + 1):
    dnm *= i
  return num / dnm

