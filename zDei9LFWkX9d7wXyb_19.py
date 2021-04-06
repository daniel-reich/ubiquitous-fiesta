
def malthusian(food_growth, pop_mult):
  curFood = 100
  curPop = 100
  year = 0
  while curPop <= curFood:
    curFood += food_growth
    curPop *= pop_mult
    year += 1
  return year

