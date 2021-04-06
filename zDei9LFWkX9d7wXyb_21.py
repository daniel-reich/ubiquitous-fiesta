
def malthusian(food_growth, pop_mult):
  for i in range(0, 1000):
      a = 100*pop_mult ** i
      b = 100 + food_growth*i
      if a > b:
          break
          print(i)
      else:
          continue
  return i

