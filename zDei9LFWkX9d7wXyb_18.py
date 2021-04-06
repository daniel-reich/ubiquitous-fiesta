
def malthusian(food_growth, pop_mult):
  YC = 0
  P, F = 100*pop_mult,100+food_growth
  while P < F:
    F += food_growth
    P *= pop_mult
    YC += 1
  return YC+1

