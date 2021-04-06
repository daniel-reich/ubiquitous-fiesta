
def prime_factors(num):
  factors = []
  target_num = num
  i = 2
  while(i <= target_num):
    if(target_num % i == 0):
      factors.append(i)
      target_num /= i
      i = 2
    else:
      i += 1
  return factors

