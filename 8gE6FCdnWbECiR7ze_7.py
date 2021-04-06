
def smith_type(n):
  if n == 1: return "Not a Smith"
  if is_prime(n): return "Trivial Smith" 
  y, up_x, down_x, x, up_y, down_y = sum(prime_factorisation(n)), n+1, n-1, n, sum(prime_factorisation(n+1)), sum(prime_factorisation(n-1))
  while x > 9: x = sum([int(y) for y in str(x)])
  while y > 9: y = sum([int(z) for z in str(y)])
  if x != y: return ("Not a Smith")
  if not is_prime(up_x):
    while up_x > 9: up_x = sum([int(y) for y in str(up_x)])
    while up_y > 9: up_y = sum([int(z) for z in str(up_y)])
    if up_x == up_y: return "Youngest Smith"
  if not is_prime(down_x):
    while down_x > 9: down_x = sum([int(y) for y in str(down_x)])
    while down_y > 9: down_y = sum([int(z) for z in str(down_y)])
    if down_x == down_y: return "Oldest Smith"
  return "Single Smith"
  
def is_prime(n):
  for x in range(2,n//2+1):
    if n % x == 0: return False
  return True
  
def prime_factorisation(num):
  x = 2
  result = []
  while not is_prime(num):
    while num % x == 0:
      result.append(x)
      num  = num  // x
    x+=1
  result.append(num)
  if 1 in result:
    del result[result.index(1)]
  return result

