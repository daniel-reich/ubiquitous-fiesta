
def sweetest_icecream(lst):
  sweetness = {'Plain':0,'Vanilla':5,'ChocolateChip':5,'Strawberry':10,'Chocolate':10}
  value = [sweetness[i.flavor] + i.num_sprinkles for i in lst]
  return max(value)

