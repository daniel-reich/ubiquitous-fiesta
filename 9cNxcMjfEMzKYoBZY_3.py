
def factors(num):
  factors = []
  for i in range(1, num):
    if num % i == 0:
      factors.append(i)
  return factors
  
def num_type(n):
  sum_factors = sum(factors(n))
  if sum_factors == n:
    return "Perfect"
  elif sum(factors(sum_factors)) == n:
    return "Amicable"
  else:
    return "Neither"

