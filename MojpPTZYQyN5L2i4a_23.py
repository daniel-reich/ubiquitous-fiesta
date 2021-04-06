
def cars(wheels, bodies, figures):
  wheelsets = wheels//4
  figuresets = figures//2
​
  return 0 if 0 in (wheelsets, figuresets, bodies) else min(wheelsets, figuresets, bodies)

