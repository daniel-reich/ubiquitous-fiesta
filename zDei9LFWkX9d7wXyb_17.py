
def malthusian(food_growth, pop_mult):
  year=0
  pop=100
  food_prod = 100
  while True:
    food_prod+=food_growth
    pop*=pop_mult
    year+=1
    if pop>food_prod:
      break
  return year

