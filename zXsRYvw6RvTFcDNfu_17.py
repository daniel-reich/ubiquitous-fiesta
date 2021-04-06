
def ruth_aaron(n):
  aaron, ruth, product, sums, ab, ac = False, False, False, False, False, False
  a_p, b_p, c_p = summ(n), summ(n+1), summ(n-1)
  if sum(a_p) == sum(b_p): sums, ab = True, True
  if sum(a_p) == sum(c_p): sums, ac = True, True
  alp, blp, clp = prods(n), prods(n+1), prods(n-1)
  if  sum(alp) == sum(blp): product, ab = True, True
  if sum(alp) == sum(clp): product, ac = True, True
  if ab: ruth, aaron = True, False
  if ac: aaron, ruth = True, False
  name =  "Aaron" if aaron else "Ruth" if ruth else 0 
  if name == 0: return False
  return [name, 3 if product and sums else 2 if product else 1]
  
  
  
def prods(y):
  ret = []
  x = 2
  while not prime(y):
    while y % x == 0: 
      ret.append(x)
      y = y// x
    x += 1
  if y > 1: ret.append(y)
  return ret
  
def summ(y):
  return [ x for x in range(2, y+1) if y % x == 0 and prime(x)]
  
def prime(n):
  return len([x for x in range(2, n//2+1) if n % x == 0]) == 0

