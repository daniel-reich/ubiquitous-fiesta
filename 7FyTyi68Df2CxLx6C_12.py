
class Pizza:
  order_number = 0
  def __init__(self, ingredients):
    self.ingredients = ingredients
    Pizza.order_number += 1
    self.order_number = Pizza.order_number
  
  def hawaiian():
    return Pizza(['ham', 'pineapple'])
  
  def meat_festival():
    return Pizza(['beef', 'meatball', 'bacon'])
    
  def garden_feast():
    return Pizza(['spinach', 'olives', 'mushroom'])

