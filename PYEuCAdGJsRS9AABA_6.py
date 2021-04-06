
class CoffeeShop:
  orders=[]
  def __init__(self, name, menu, orders):
    self.name=name
    self.menu=menu
    self.orders=orders
  def add_order(self, item):
    M=[x['item'] for x in self.menu]
    if item in M:
      self.orders.append(item)
      return "Order added!"
    else:
      return "This item is currently unavailable!"
  def fulfill_order(self):
    if self.orders:
      return "The {} is ready!".format(self.orders.pop(0))
    else:
      return "All orders have been fulfilled!"
  def list_orders(self):
    return self.orders
  def due_amount(self):
    s=0
    for x in self.orders:
      for y in self.menu:
        if y['item']==x:
          s+=y['price']
    return round(s,2)
  def cheapest_item(self):
    A=[]
    for y in self.menu:
      A.append((y['item'],y['price']))
    if A:
      return sorted(A, key=lambda x: x[1])[0][0]
    
  def drinks_only(self):
    B=[]
    for y in self.menu:
      if y['type']=="drink":
        B.append(y['item'])
    return B
  def food_only(self):
    B=[]
    for y in self.menu:
      if y['type']=="food":
        B.append(y['item'])
    return B

