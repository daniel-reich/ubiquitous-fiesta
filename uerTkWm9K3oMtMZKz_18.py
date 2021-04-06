
def sweetest_icecream(lst):
  flav = {"Plain":  0, "Vanilla": 5, "ChocolateChip": 5, "Strawberry": 10, "Chocolate" : 10}
  return max([i.num_sprinkles + flav[i.flavor] for i in lst])

