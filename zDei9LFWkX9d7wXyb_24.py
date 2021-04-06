
def malthusian(food_growth, pop_mult):
  f = 100
  p = 100
  year = 1
  while p <= f:
    f += food_growth
    p *= pop_mult
    year += 1
  return year -1

