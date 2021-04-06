
class Pizza:
  order = 0
  def __init__(self, ingredients):
    self.ingredients = ingredients
    Pizza.order += 1
    self.order_number = Pizza.order
    
  @classmethod
  def hawaiian(class_object):
    ingredients = ["ham", "pineapple"]
    return class_object(ingredients)
    
  @classmethod
  def meat_festival(class_object):
    ingredients = ["beef", "meatball", "bacon"]
    return class_object(ingredients)
    
  @classmethod
  def garden_feast(class_object):
    ingredients = ["spinach", "olives", "mushroom"]
    return class_object(ingredients)

