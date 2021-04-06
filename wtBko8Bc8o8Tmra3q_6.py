
def halflife_calculator(mass, hlife, n):
  for i in range(n):
    mass=mass/2
  return [round(mass,3),hlife*n]

