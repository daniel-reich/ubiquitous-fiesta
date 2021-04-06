
def malthusian(food_growth, pop_mult):
  d={"food_prod": 100, "pop": 100, "year": 0}
  
  while d["pop"] <= d['food_prod']:
    d["food_prod"] += food_growth
    d["pop"] *= pop_mult
    d["year"] += 1
  return d["year"]

