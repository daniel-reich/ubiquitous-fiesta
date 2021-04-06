
class Pizza:
  ORDER = 0
  
  def __init__(self, ingredients):
    Pizza.ORDER += 1
    self.order_number = Pizza.ORDER
    self.ingredients = ingredients
    
  def hawaiian():
    return Pizza(['ham', 'pineapple'])
​
  def meat_festival():
    return Pizza(['beef', 'meatball', 'bacon'])
  
  def garden_feast():
    return Pizza(['spinach', 'olives', 'mushroom'])

