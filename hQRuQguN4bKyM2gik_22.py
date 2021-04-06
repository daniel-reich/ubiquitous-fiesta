
def simple_check(a, b):
  count = 0
  while a > 0 and b > 0:
    if max([a, b]) % min([a, b]) == 0:
      count += 1
      
    a -= 1
    b -= 1
    
  return count

