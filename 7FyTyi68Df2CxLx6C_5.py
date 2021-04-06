
class Pizza:
  num_orders = 0
  def __init__(self, ingredients):
    Pizza.num_orders += 1
    self.ingredients = ingredients
    self.order_number = Pizza.num_orders
    
  def garden_feast():
    return Pizza(["spinach", "olives", "mushroom"])
    
  def meat_festival():
    return Pizza(["beef", "meatball", "bacon"])
    
  def hawaiian():
    return Pizza(["ham", "pineapple"])

