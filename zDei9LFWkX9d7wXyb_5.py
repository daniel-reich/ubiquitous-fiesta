
def malthusian(food_growth, pop_mult):
  year = 0
  food_prod = 100
  population = 100
  
  while food_prod >= population:
    year += 1
    food_prod += food_growth
    population *= pop_mult
    
  return year

