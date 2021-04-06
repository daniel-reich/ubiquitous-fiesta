
def factorial(num, fr = 0):
  return 1 if num == fr else num*factorial(num-1, fr)
​
def nPr(n, r):
  return factorial(n, n-r)
​
def nCr(n, r):
  mxs = sorted([r, n-r])
  return factorial(n, mxs[1])/factorial(mxs[0])

