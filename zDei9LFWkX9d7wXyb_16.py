
def malthusian(food_growth, pop_mult):
  food,pop=100,100
  c=0
  while food>=pop:
    food+=food_growth
    pop*=pop_mult
    c+=1
  return c

