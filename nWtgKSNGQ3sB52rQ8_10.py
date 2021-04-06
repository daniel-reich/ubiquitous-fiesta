
def evenly_divisible(a, b, c):
  result = 0
  for i in range(a,b+1):
    if i % c == 0:
      result += i
  
  return result

