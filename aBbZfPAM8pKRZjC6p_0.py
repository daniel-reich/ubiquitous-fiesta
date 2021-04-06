
def fruit_salad(fruits):
  salad = []
  for fruit in fruits:
    mid = len(fruit) // 2
    salad += [fruit[:mid], fruit[mid:]]
  return ''.join(sorted(salad))

