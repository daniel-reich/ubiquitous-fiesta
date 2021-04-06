
class Smoothie:
  prices = {"Strawberries": 1.5, "Banana": .5, "Mango": 2.5, "Blueberries": 1, "Raspberries":1, "Apple": 1.75, "Pineapple": 3.5}
  
  def __init__(self,ingr=list):
    self.ingredients = ingr
    self.tag = "Fusion" if len(ingr) > 1 else "Smoothie"
    self.cost = sum(self.prices.get(fruit) for fruit in self.ingredients)
    
  def get_name(self):
    return " ".join([x[:-3] + "y" if x.endswith("ies") else x for x in sorted(self.ingredients)] + [self.tag])
​
  def get_cost(self):
    return "${:,.2f}".format(self.cost)
​
  def get_price(self):
    return "${:,.2f}".format(self.cost * 2.5)

