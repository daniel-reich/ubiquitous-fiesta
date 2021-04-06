
def malthusian(food_growth, pop_mult):
  food, pop, year = 100, 100, 0
  while food >= pop:
    food += food_growth
    pop *= pop_mult
    year += 1
  return year

