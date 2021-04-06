
def funny_numbers(n, p):
  
  find_k = lambda prod, n: prod / n if prod / n == prod // n else None
  sum_of_digits_to_power_p = lambda n, p: sum([int(num) ** p.pop(0) for num in str(n)])
  pp = list(range(p, p + len(str(n))))
  
  sodtpp = sum_of_digits_to_power_p(n, pp)
  
  return find_k(sodtpp, n)

