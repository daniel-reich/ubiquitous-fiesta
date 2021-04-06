
class Pizza:
  order_number = 1
  def __init__(self, ingredients):
    self.order_number = Pizza.order_number
    Pizza.order_number += 1
    self.ingredients = ingredients
    
  @classmethod
  def garden_feast(cls):
    ingredients = ["spinach", "olives", "mushroom"]
    return  cls(ingredients)
  @classmethod
  def hawaiian(cls):
    ingredients = ["ham", "pineapple"]
    return  cls(ingredients)
  @classmethod
  def meat_festival(cls):
    ingredients = ["beef", "meatball", "bacon"]
    return cls(ingredients)

