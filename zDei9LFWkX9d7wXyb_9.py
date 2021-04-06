
def malthusian(food_growth, pop_mult):
  for x in range(0,1000000):
    if (food_growth*x+100) < (100*(pop_mult)**x):
      return x

