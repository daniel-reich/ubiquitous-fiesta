
def halflife_calculator(mass, hlife, n):
  x = (hlife * n)
  while n > 0:
    mass = mass / 2
    n -= 1
  return [round(mass, 3) ,x]

