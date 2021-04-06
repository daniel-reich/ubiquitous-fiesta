
class CoffeeShop:
  def __init__(self, name, menu, orders):
    self.name = name
    self.menu = menu
    self.orders = orders
    
  def add_order(self, order_item):
    for dish in self.menu:
      if dish['item'] == order_item:
        self.orders.append(order_item)
        return 'Order added!'
    return "This item is currently unavailable!"
    
  def fulfill_order(self):
    if self.orders:
      return 'The {} is ready!'.format(self.orders.pop(0))
    return "All orders have been fulfilled!"
    
  def list_orders(self):
    return self.orders
    
  def due_amount(self):
    out = 0
    for order in self.orders:
      for dish in self.menu:
        if dish['item'] == order:
          out += dish['price']
    return round(out, 2)
    
  def cheapest_item(self):
    return min(self.menu, key=lambda x: x['price'])['item']
    
  def drinks_only(self):
    return [dish['item'] for dish in self.menu if dish['type'] == 'drink']
    
  def food_only(self):
    return [dish['item'] for dish in self.menu if dish['type'] == 'food']

