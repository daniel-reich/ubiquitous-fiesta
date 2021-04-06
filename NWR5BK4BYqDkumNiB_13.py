
from functools import reduce
​
def digital_division(n):
  lst = list(str(n).replace("0", ""))
  divisible_by_each = True if len([i for i in lst if n % int(i) == 0]) == len(str(n)) else False
  divisible_by_sum = True if n % sum([int(i) for i in lst]) == 0 else False
  divisible_by_product = True if n % reduce(lambda a, b: a * b, [int(i) for i in lst]) == 0 else False
  divisible = [divisible_by_each, divisible_by_sum, divisible_by_product]
  if all(divisible):
      return "Perfect"
  elif not any(divisible):
      return "Indivisible"
  return divisible.count(True)

