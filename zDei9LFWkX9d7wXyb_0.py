
def malthusian(food_growth, pop_mult):
  x,f,p = 0,100,100
  while f>=p:
    f += food_growth
    p *= pop_mult
    x += 1
  return x

