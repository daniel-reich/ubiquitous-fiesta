
def num_type(num):
  factors = sum([f for f in range(1,num) if num%f == 0])
  rev_factors = sum([f for f in range(1,factors) if factors%f == 0])
  
  if num == factors:
    return 'Perfect'
  elif num == rev_factors:
    return 'Amicable'
  else:
    return "Neither"

