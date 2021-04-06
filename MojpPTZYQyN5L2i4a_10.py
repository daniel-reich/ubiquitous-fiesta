
def cars(wheels, bodies, figures):
  minWheels = wheels // 4
  minFigures = figures // 2
  
  return min(minWheels, bodies, minFigures)

