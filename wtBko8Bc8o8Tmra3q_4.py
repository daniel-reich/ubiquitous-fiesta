
def halflife_calculator(mass, hlife, n):
  c = n
  while c > 0:
    mass /= 2
    c -= 1
  return [round(mass, 3), n * hlife]

