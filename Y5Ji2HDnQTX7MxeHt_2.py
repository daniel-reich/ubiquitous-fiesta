
def snakefill(n):
  #snake length * 2 when food += 1
  s_length = 1
  food = 0
  
  #when length > n*n, output food
  while s_length <= n*n:
    food += 1
    s_length = s_length * 2
    
  return (food-1)

