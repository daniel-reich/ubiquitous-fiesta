
def cars(wheels, bodies, figures):
  ##need 4 wheels, 1 body, 2 figures
  cars = 0
  while wheels >=4 and bodies >= 1 and figures >=2:
    cars += 1
    wheels -= 4
    bodies -= 1
    figures -= 2
  
  return cars

