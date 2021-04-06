
def automorphic(n):
  sqr = n**2
  num = len(str(n))
  last = sqr%pow(10,num)
  return last == n

