
def malthusian(food_growth, pop_mult):
  year = 0
  food = 100
  population = 100
  while food >= population:
    food = 100 + (food_growth * year)
    population = 100 * (pop_mult)**year
    year += 1
  return year-1

