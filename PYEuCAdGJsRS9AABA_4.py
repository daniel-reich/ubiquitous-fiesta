
class CoffeeShop:
  def __init__(self, name, menu, orders):
    self.name = name
    self.menu = menu
    self.orders = orders
  
  def add_order(self,order):
    if order in [i['item'] for i in self.menu]:
      self.orders.append(order)
      return "Order added!"
    else:
      return "This item is currently unavailable!"
    
  def fulfill_order(self):
    if len(self.orders)>0:
      return "The {0} is ready!".format(self.orders.pop(0))
    else:
      return "All orders have been fulfilled!"
      
  def list_orders(self):
    return self.orders
  
  def due_amount(self):
    return round(sum(i['price']*self.orders.count(i['item']) for i in self.menu),2)
    
  def cheapest_item(self):
    return min(self.menu, key=lambda x:x['price'])['item']
    
  def drinks_only(self):
    return [i['item'] for i in self.menu if i['type']=='drink']
    
  def food_only(self):
    return [i['item'] for i in self.menu if i['type']=='food']

