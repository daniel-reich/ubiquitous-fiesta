
class Pizza:
  count_orders=0
  def __init__(self, ingredients):
    self.ingredients = ingredients
    Pizza.count_orders+=1
    self.order_number=Pizza.count_orders
  
  @staticmethod
  def garden_feast():
      ingredients=['spinach', 'olives', 'mushroom']
      return Pizza(ingredients)
      
  @staticmethod   
  def hawaiian():
      ingredients=['ham', 'pineapple']
      return Pizza(ingredients)
  
  @staticmethod   
  def meat_festival():
      ingredients=['beef', 'meatball', 'bacon']
      return Pizza(ingredients)

