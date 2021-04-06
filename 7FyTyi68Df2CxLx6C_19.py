
class Pizza:
​
  counter = 0
​
  def __init__(self, ingredients = None):
    type(self).counter += 1
    self.order_number = type(self).counter
    self.ingredients = ingredients
​
  def __del__(self):
    type(self).counter -= 1
  
  def hawaiian():
    return Pizza('ham, pineapple'.split(', '))
​
  def meat_festival():
    return Pizza('beef, meatball, bacon'.split(', '))
  
  def garden_feast():
    return Pizza('spinach, olives, mushroom'.split(', '))

