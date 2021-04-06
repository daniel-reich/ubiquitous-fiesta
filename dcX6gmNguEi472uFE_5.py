
def double_factorial(num):
  even_total = 1
  odd_total  = 1
  if num <= 0:
    return 1
  
  for i in range(1, num + 1):
    if i % 2:
      odd_total *= i
    if i % 2 == 0:
      even_total *= i
    
  return even_total if num % 2 == 0 else odd_total

