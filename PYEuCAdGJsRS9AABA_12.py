
class CoffeeShop:
  def __init__(self, name, menu, orders):
    self.name = name
    self.menu = menu
    self.orders = orders
    self.items = [m['item'] for m in menu]
    
  def add_order(self, order):
    if order in self.items:
      self.orders.append(order)
      return 'Order added!'
    return 'This item is currently unavailable!'
    
  def fulfill_order(self):
    if self.orders:
      order = self.orders[0]
      self.orders = self.orders[1:]
      return 'The {} is ready!'.format(order)
    return 'All orders have been fulfilled!'
  
  def list_orders(self):
    return self.orders
  
  def due_amount(self):
    amt = 0
    for order in self.orders:
      for m in self.menu:
        if order == m['item']: amt += m['price']
    return round(amt, 2)
  
  def cheapest_item(self):
    return min(self.menu, key=lambda m: m['price'])['item']
    
  def drinks_only(self):
    return [m['item'] for m in self.menu if m['type'] == 'drink']
    
  def food_only(self):
    return [m['item'] for m in self.menu if m['type'] == 'food']

