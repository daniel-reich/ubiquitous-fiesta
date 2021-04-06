
def is_prime(n):
  if n <= 1: return False
  for i in range(2, n):
    if not n % i: return False
  return True 
​
def how_bad(n):
  p = bin(n)[2:].count('1')
  result = []
  if not p % 2: result.append('Evil')
  else: result.append('Odious')
  if is_prime(p):
    result.append('Pernicious')
  return result

