
class Pizza:
  orders = 0
  def __init__(self, ingredients):
    self.ingredients = list(ingredients)
    self.order_number = self.get_order_number()
    
  def get_order_number(self):
    Pizza.orders += 1
    return Pizza.orders
    
  def garden_feast():
    return Pizza(['spinach', 'olives', 'mushroom'])
    
  def hawaiian():
    return Pizza(['ham', 'pineapple'])
    
  def meat_festival():
    return Pizza(['beef', 'meatball', 'bacon'])

