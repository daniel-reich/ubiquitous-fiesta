
def malthusian(food_growth, pop_mult):
  count, pop, food = 0, 100, 100
  while pop <= food:
    food += food_growth
    pop *= pop_mult
    count += 1
  return count

