
def cars(wheels, bodies, figures):
  i = 0
  numwheels = wheels
  numbodies = bodies
  numfigures = figures
  while (numwheels >= 4) and (numbodies >= 1) and (numfigures >= 2):
    i += 1
    numwheels -= 4
    numbodies -= 1
    numfigures -= 2
  return i

