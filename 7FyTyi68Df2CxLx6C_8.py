
order_number = 0
class Pizza:
  def __init__(self, ingredients):
    global order_number
    self.ingredients = ingredients
    order_number += 1
    self.order_number = order_number 
  def garden_feast():
    a = Pizza(['spinach', 'olives', 'mushroom'])
    return a
  def hawaiian():
    a = Pizza(['ham', 'pineapple'])
    return a
  def meat_festival():
    a = Pizza(['beef', 'meatball', 'bacon'])
    return a

