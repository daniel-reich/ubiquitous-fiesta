
def points_in_circle(points, centerX, centerY, radius):
  r2 = radius ** 2
  #d2 = (points[0]["x"] - centerX) **2 + (points[0]["y"] - centerY) ** 2
  count = 0
​
  for i in points:
    d2 = (i["x"] - centerX) **2 + (i["y"] - centerY) ** 2
    if d2 < r2:
      count += 1
  return count

