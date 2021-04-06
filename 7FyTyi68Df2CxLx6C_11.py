
class Pizza:
  order_number = 0
  
  def __init__(self, ingredients):
    self.ingredients = ingredients
    Pizza.order_number += 1
    self.order_number = Pizza.order_number
  
  @classmethod
  def garden_feast(Pizza):
    return Pizza(["spinach", "olives", "mushroom"])
  
  @classmethod
  def hawaiian(Pizza):
    return Pizza(["ham", "pineapple"])
  
  @classmethod
  def meat_festival(Pizza):
    return Pizza(["beef", "meatball", "bacon"])

