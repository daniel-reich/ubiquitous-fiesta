
def ways_to_climb(n):
  if n == 0:
    return 1
  if n < 3:
    return n
  
  return ways_to_climb(n-1) + ways_to_climb(n-2)

