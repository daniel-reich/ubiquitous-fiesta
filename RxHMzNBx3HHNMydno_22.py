
def total_distance(height, length, tower):
  steps = tower / height
  return round(steps * (height + length), 1)

