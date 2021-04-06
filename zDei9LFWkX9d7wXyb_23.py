
def malthusian(food_growth, pop_mult):
  food, pop = 100, 100
  years = 1
  while True:
    food += food_growth
    pop *= pop_mult
    if pop <= food:
      years += 1
    if pop > food:
      return years

