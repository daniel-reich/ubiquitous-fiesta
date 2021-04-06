
class CoffeeShop:
  def __init__(self, name, menu, orders):
    self.name = name
    self.menu = menu
    self.orders = orders
  
  def add_order(self, item):
    if item in [i["item"] for i in self.menu]:
      self.orders.append(item)
      return "Order added!"
    else:
      return "This item is currently unavailable!"
    
  def fulfill_order(self):
    if len(self.orders) != 0:
      fulfilled_order = self.orders[0]
      self.orders = self.orders[1:]
      return "The " + fulfilled_order + " is ready!"
    else:
      return "All orders have been fulfilled!"
      
  def list_orders(self):
    return self.orders
  
  def due_amount(self):
    total = 0
    for i in self.orders:
      for j in self.menu:
        if j["item"] == i:
          total += j["price"]
          break
    return round(total,2)
  
  def cheapest_item(self):
    lowest_price = min([i["price"] for i in self.menu])
    for i in self.menu:
      if i["price"] == lowest_price:
        return i["item"]
  
  def drinks_only(self):
    return [i["item"] for i in self.menu if i["type"] == "drink"]
    
  def food_only(self):
    return [i["item"] for i in self.menu if i["type"] == "food"]

