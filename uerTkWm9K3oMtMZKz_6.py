
class IceCream:
  def __init__(self, flavor, num_sprinkles):
    self.flavor = flavor
    self.num_sprinkles = num_sprinkles
​
my_dict = {"Chocolate": 10, "Vanilla": 5, "Strawberry": 10, "Plain": 0, "ChocolateChip": 5}
​
def sweetest_icecream(lst):
  return max([(my_dict[item.flavor] + item.num_sprinkles) for item in lst])

