
def malthusian(food_growth, pop_mult):
  food = 100
  pop = 100
  counter = 0
  while pop <= food:
    food = food + food_growth
    pop = pop * pop_mult
    counter +=1
  return counter

