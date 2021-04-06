
def ways_to_climb(n):
  # Fibonacci 
  if n<2:
    return 1
  return ways_to_climb(n-1) + ways_to_climb(n-2)

