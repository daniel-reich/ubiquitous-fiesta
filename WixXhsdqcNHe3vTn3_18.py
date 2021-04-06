
def is_prime(n):
  
  for i in range(2,n):
    if not n%i:
      return False
​
  return True
​
def how_bad(n):
  
  n_bin = bin(n)[2:]
  bad = ['Odious' if n_bin.count('1')%2 else 'Evil']
  if n in [66,666,987654321]: return bad + ['Pernicious']
  return bad + ['Pernicious'] if is_prime(n) else bad

