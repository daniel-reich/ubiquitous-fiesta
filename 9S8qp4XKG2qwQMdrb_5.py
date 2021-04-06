
def ways_to_climb(n):
  return 1 if n in [0, 1] else ways_to_climb(n-1)+ways_to_climb(n-2)

