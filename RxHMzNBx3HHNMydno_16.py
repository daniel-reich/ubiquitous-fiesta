
def total_distance(height, length, tower):
  stairs = tower / height
  distance = stairs * (height + length)
  return round(distance, 1)

