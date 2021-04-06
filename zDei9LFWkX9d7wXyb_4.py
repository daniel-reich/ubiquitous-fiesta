
def malthusian(food_growth, pop_mult):
  food,pop=100,100;y=0
  while pop<=food:
    food+=food_growth
    pop*=pop_mult
    y+=1
  return y

