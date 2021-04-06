
def sweetest_icecream(lst):
  x = {'Plain':0, 'Vanilla':5, 'ChocolateChip':5, 'Strawberry':10, 'Chocolate':10}
  s = 0;
  for elem in lst:
    s = max( x[elem.flavor] + elem.num_sprinkles, s)
  return s

