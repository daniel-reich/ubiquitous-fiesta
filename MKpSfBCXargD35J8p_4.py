
def journey_distance(n):
  if n == 0:
    return 0
  elif n <= 3:
    return 1
  else:
    return 1 + ((n-3) / 2)

