
def logarithm(base, num):
  bad_base = [-1, 0, 1]
  if base in bad_base:
    return "Invalid"
  
  if num <= 0:
    return "Invalid"
    
  for exp in range(100):
    if base ** exp == num:
      return exp

