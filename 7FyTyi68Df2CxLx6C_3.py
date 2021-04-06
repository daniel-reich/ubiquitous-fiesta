
class Pizza:
  
  orders = 0
  
  def __init__ (self, ingredients):
    Pizza.orders +=1
    self.order_number = Pizza.orders
    self.ingredients = ingredients
​
  def hawaiian():
    return Pizza(["ham", "pineapple"])
​
  def meat_festival():
    return Pizza(["beef", "meatball", "bacon"]) 
    
  def garden_feast():
    return Pizza(["spinach", "olives", "mushroom"])

