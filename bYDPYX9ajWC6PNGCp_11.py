
def track_robot(*steps):
  x = 0
  y = 0
  steps = list(steps)
  for i in range(0,len(steps)):
    if i % 4 == 0:
      y += steps[i]
    elif i % 4 == 1:
      x += steps[i]
    elif i % 4 == 2:
      y -= steps[i]
    else:
      x -= steps[i]
  return [x,y]

