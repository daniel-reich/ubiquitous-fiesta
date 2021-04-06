
def sweetest_icecream(lst):
  equiv = {'Plain':0, 'Vanilla':5, 'ChocolateChip':5, 'Chocolate':10, 'Strawberry':10}
  return max([equiv[self.flavor]+self.num_sprinkles for self in lst])

