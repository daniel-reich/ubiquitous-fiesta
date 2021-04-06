
def track_robot(*steps):
  x, y = 0, 0
  for a in range(len(steps)):
    step = steps[a]
    if a % 2 == 1:
      if a % 4 == 1:
        x += step
      else:
        x -= step
    else:
      if a % 4 == 0:
        y += step
      else:
        y -= step
  return [x, y]

