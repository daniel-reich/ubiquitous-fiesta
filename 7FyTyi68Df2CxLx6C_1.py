
class Pizza:
  __orders = 0
  def __init__(self, ingredients):
    self.order_number = self.OrderNumber()
    self.ingredients = ingredients
  @staticmethod
  def OrderNumber():
    Pizza.__orders += 1
    return Pizza.__orders
  @classmethod
  def hawaiian(cls):
    return cls(['ham', 'pineapple'])
  @classmethod
  def meat_festival(cls):
    return cls(['beef', 'meatball', 'bacon'])
  @classmethod
  def garden_feast(cls):
    return cls(['spinach', 'olives', 'mushroom'])

