
def halflife_calculator(mass, hlife, n):
  i = 0
  years = 0
  final_mass = mass
  return [round(mass*pow(1/2,n),3), hlife*n]

