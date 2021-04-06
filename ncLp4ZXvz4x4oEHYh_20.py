
def sum_of_two(a, b, v):
  from itertools import product 
  return v in [sum(sub) for sub in product(a,b)]

