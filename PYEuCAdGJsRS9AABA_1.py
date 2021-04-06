
class CoffeeShop:
  
  def __init__(self, name, menu, orders):
    self.name = name
    self.menu = menu
    self.orders = orders
  
  def add_order(self, order):
    for dic in self.menu:
      if order == dic['item']:
        self.orders.append(order)
        return 'Order added!'
    return "This item is currently unavailable!"
  
  def fulfill_order(self):
    if len(self.orders) == 0:
      return "All orders have been fulfilled!"
    else:
      tr = 'The {} is ready!'.format(self.orders[0])
      self.orders.pop(0)
      return tr
  
  def list_orders(self):
    return self.orders
  
  def due_amount(self):
    amount = 0
    for dic in self.menu:
      if dic['item'] in self.orders:
        amount += dic['price']
    return round(amount,2)
  
  def cheapest_item(self):
    lowest = 1000
    lowest_name = None
    for dic in self.menu:
      if dic['price'] < lowest:
        lowest = dic['price']
        lowest_name = dic['item']
    return lowest_name
  
  def drinks_only(self):
    return [drink['item'] for drink in self.menu if drink['type'] == 'drink']
  
  def food_only(self):
    return [food['item'] for food in self.menu if food['type'] == 'food']

