
def points_in_circle(points, centerX, centerY, radius):
  count = 0
  for point in points:
    if ((point["x"] - centerX)**2 + (point["y"] - centerY)**2)**0.5 < radius: count += 1
  return count

