
class Pizza:
  orders = 0
  def __init__(self, ingredients):
    self.ingredients = ingredients
    Pizza.orders += 1
    self.order_number = Pizza.orders
  @staticmethod
  def hawaiian():
    return Pizza(["ham", "pineapple"])
  @staticmethod
  def meat_festival():
    return Pizza(["beef", "meatball", "bacon"])
  @staticmethod
  def garden_feast():
    return Pizza(["spinach", "olives", "mushroom"])

