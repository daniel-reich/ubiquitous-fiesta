
def halflife_calculator(mass, hlife, n):
  num = 2**n
  Remaining = mass/num
  Remaining = round(Remaining,3)
  Years = hlife*n
  return [Remaining, Years]

