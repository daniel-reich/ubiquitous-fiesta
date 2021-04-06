
def prime_factorize(num): 
  if num == 1:
    return []
  i = 2
  while i < num:
    if num%i == 0:      
      break
    i += 1  
  
  return [i]+prime_factorize(num//i)

