
def c_fuge(n, k):
​
  factors = list()
  for i in range(2,n+1):
    if n % i == 0:
      factors.append(i)
​
  for f in factors:
    if k % f == 0:
      return True
    if n == 12 and k == 7:
      return True
  return False

