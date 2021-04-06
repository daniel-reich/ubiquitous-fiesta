
def track_robot(instructions):
  x = 0
  y = 0
  for i in instructions:
    direction = i.split()
    if direction[0] == 'up':
      y += int(direction[1])
    elif direction[0] == 'down':
      y -= int(direction[1])
    elif direction[0] == 'left':
      x -= int(direction[1])
    else:
      x += int(direction[1])
  return [x,y]

