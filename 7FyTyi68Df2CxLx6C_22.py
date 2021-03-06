
class Pizza:
  order_number = 1
  
  def __init__(self,ingredients):
    self.ingredients = ingredients
    self.order_number = Pizza.order_number
    self.__class__.order_number += 1
  
  @classmethod
  def garden_feast(cls):
    return cls(['spinach', 'olives', 'mushroom'])
  
  @classmethod
  def hawaiian(cls):
    return cls(['ham', 'pineapple'])
  
  @classmethod
  def meat_festival(cls):
    return cls(['beef', 'meatball', 'bacon'])

