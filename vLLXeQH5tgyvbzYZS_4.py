
def is_prim_pyth_triple(lst):
  a, b, c = sorted(lst)
  if a**2 + b**2 == c**2:
    a_f = get_prime_factors(a)
    b_f = get_prime_factors(b)
    c_f = get_prime_factors(c)
    
    if not a_f & b_f & c_f:
      return True
  return False
​
def get_prime_factors(n):
  facts = set()
  for i in range(2,n):
    while not n%i:
      if i not in facts:
        facts.add(i)
      n //= i
  return facts

