
def prime_factors(num):
  lst = list()
  first_factor = 2
  while num > 1:
    if num%first_factor == 0:
      lst.append(first_factor)
      num /= first_factor
    else:
      first_factor += 1
  
  return lst

