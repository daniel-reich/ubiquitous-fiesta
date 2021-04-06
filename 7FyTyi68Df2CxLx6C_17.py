
from itertools import count
class Pizza:
  orders=0
  def __init__(self,lst):
    self.ingredients = lst
    Pizza.orders+=1
    self.order_number=Pizza.orders
    
  def hawaiian():
    return Pizza(['ham','pineapple'])
    
  def meat_festival():
    return Pizza(['beef','meatball','bacon'])
    
  def garden_feast():
    return Pizza(['spinach','olives','mushroom'])

