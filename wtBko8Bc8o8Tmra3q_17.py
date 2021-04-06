
def halflife_calculator(mass, hlife, n):
  final_mass = round(mass / 2**n, 3)
  years = hlife * n
  return [final_mass, years]

