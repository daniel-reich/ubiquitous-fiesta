
def malthusian(food_growth, pop_mult, food=100, pop=100):
  if food < pop:
    return 0
  return 1 + malthusian(food_growth,pop_mult, food+food_growth, pop*pop_mult)

