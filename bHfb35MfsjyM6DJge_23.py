
def route_diff(directions):
  stepCount = 0
  xCount = 0
  yCount = 0
  for i in directions:
    stepCount = stepCount + 1
    if i == 'N':
      xCount = xCount + 1
    elif i == 'S':
      xCount = xCount - 1
    elif i == 'E':
      yCount = yCount + 1
    else:
      yCount = yCount - 1
  return stepCount - (abs(xCount) + abs(yCount))

