
class CoffeeShop:
  def __init__(self, name, menu, orders):
    self.name = name
    self.menu = menu
    self.orders = orders
    
  def add_order(self, order):
    for item in self.menu:
      if item['item'] == order:
        self.orders.append(order)
        return "Order added!"
    return "This item is currently unavailable!"
  
  def fulfill_order(self):
    if len(self.orders) < 1: return "All orders have been fulfilled!"
    return "The {0} is ready!".format(self.orders.pop(0))
  
  list_orders = lambda self: self.orders
  
  def due_amount(self):
    return round(sum(i['price'] for i in self.menu if i['item'] in self.orders), 2)
    
  def cheapest_item(self):
    return min(self.menu, key = lambda i: i['price'])['item']
    
  def drinks_only(self):
    return [i['item'] for i in self.menu if i['type'] == "drink"]
    
  def food_only(self):
    return [i['item'] for i in self.menu if i['type'] == "food"]

