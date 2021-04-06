
def cars_needed(n):
  if n == 0 : 
    return 0 
  elif n % 5 == 0 : 
    return (n // 5)
  else : 
    return (n // 5) + 1

