
def ways_to_climb(n):
  if n == 0:
    return 1
  elif n == 1:
    return 1
  else:
    return ways_to_climb(n-1) + ways_to_climb(n-2)

