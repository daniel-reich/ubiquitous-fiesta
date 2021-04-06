
def sweetest_icecream(lst):
  d = {'Plain': 0, 'Vanilla': 5, 'ChocolateChip': 5, 'Strawberry': 10, 'Chocolate': 10}
  return max(map(lambda x: d[x.flavor] + x.num_sprinkles, lst))

