
class CoffeeShop:
  def __init__(self, name,  menu, orders):
    self._name = name
    self._menu = menu
    self._orders = orders
​
  def shop_name(self):
    return self._name
​
  def add_order(self, item):
    if any(m['item'] == item for m in self._menu):
      self._orders += [item]
      return 'Order added!'
    return 'This item is currently unavailable!'
​
  def fulfill_order(self):
    return "The {0} is ready!".format(self._orders.pop(0)) \
      if len(self._orders) else 'All orders have been fulfilled!'
​
  def list_orders(self):
    return self._orders
​
  def due_amount(self):
    items = filter(lambda x: x['item'] in self._orders, self._menu)
    return round(sum(item['price'] for item in items)*100)/100
​
  def cheapest_item(self):
    return [x['item'] for x in self._menu
      if x['price'] == min(*[x['price'] for x in self._menu])].pop()
​
  def drinks_only(self):
    return [x['item'] for x in self._menu if x['type'] == 'drink']
​
  def food_only(self):
    return [x['item'] for x in self._menu if x['type'] == 'food']

