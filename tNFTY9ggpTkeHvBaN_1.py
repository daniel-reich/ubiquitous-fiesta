
def total_volume(*boxes):
  total = sum([i * j * k for i, j, k in boxes])
  return total

