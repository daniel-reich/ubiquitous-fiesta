
class CoffeeShop:
  def __init__(self, name, menu, orders):
    self.name=name
    self.menu=menu
    self.orders=orders
  def add_order(self,item):
    if item in [i['item'] for i in self.menu]:
      self.orders.append(item)
      return 'Order added!'
    else:
      return 'This item is currently unavailable!'
  def fulfill_order(self):
    if self.orders:
      order = self.orders[0]
      self.orders = self.orders[1:]
      return 'The '+order+' is ready!'
    else:
      return 'All orders have been fulfilled!'
  list_orders = lambda self: self.orders
  def due_amount(self):
    return round(sum([sum([i['price'] for i in self.menu if i['item']==j]) for j in self.orders]),2)
  def cheapest_item(self):
    return [i['item'] for i in self.menu if i['price']==min([j['price'] for j in self.menu])][0]  
  def drinks_only(self):
    return [i['item'] for i in self.menu if i['type']=='drink']
  def food_only(self):
    return [i['item'] for i in self.menu if i['type']=='food']

