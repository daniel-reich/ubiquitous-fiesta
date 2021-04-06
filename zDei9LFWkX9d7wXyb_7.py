
def malthusian(food_growth, pop_mult):
  a = 100
  b = 100
  c = 0
  while a >= b:
      c += 1
      a += food_growth
      b *= pop_mult
  return c

