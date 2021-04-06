
class Smoothie:
​
  def __init__(self, ingredients):
      self.ingredients = ingredients
      self.fruit = {"strawberries": 1.50,
                    "banana":       0.50,
                    "mango":        2.50,
                    "blueberries":  1.00,
                    "raspberries":  1.00,
                    "apple":        1.75,
                    "pineapple":    3.50}
​
  def get_cost(self):
      return "$%.2f" % round(sum([self.fruit[fruit.lower()] for fruit in self.ingredients]), 2)
​
  def get_price(self):
      cost = float(self.get_cost().replace("$", ""))
      return "$%.2f" % round((cost * 1.50) + cost, 2)
​
  def get_name(self):
      return "{} Smoothie".format(self.ingredients[0]).replace("berries", "berry") if len(self.ingredients) == 1 else\
             "{} Fusion".format(" ".join(sorted(self.ingredients)).replace("berries", "berry"))

