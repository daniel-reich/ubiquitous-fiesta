
def total_distance(height, length, tower):
  num_stair = tower/height
  distance = tower + length * num_stair
  return round(distance, 1)

