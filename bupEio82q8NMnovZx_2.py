
def track_robot(instructions):
  x = 0
  y = 0
  for entry in instructions:
    cmmnd = entry.split()
    direc = cmmnd[0]
    dist = int(cmmnd[1])
    if direc == "right":
      x += dist
    elif direc == "left":
      x -= dist
    elif direc == "up":
      y += dist
    elif direc == "down":
      y -= dist
  return [x,y]

