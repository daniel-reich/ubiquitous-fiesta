
def malthusian(food_growth, pop_mult):
  food = 100
  pop = 100
  count_years = 0
  while food>=pop:
    food += food_growth
    pop = pop*pop_mult
    count_years+=1
  return count_years

