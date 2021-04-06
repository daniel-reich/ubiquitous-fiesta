
def fruit_salad(fruits):
  result = []
  for fruit in fruits:
    half_size = len(fruit)//2   
    result += [fruit[:half_size], fruit[half_size:]]
  return ''.join(sorted(result))

