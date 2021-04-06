
def halflife_calculator(mass, hlife, n):
  for d in range(n):
    mass=mass*0.5
  y=hlife*n
  x=round(mass,3)
  return([x, y])

