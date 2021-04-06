
def route_diff(directions):
  xpos = 0
  ypos = 0
  for step in directions:
    if step == 'W':
      xpos -= 1
    if step == 'E':
      xpos += 1
    if step == 'N':
      ypos += 1
    if step == 'S':
      ypos -= 1
  end = abs(xpos) + abs(ypos)
  return len(directions) - end

