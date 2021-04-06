
def can_fit(weights, bags):
  class Bag:
​
    def __init__(self, maxweight, ident, inventory = []):
      self.i = inventory
      self.w = 0
      self.id = ident
​
      for item in inventory:
        self.w += item.w
      
      self.mw = maxweight
      self.available = self.mw - self.w
​
    def add(self, item):
      if item.w <= self.available and item.b == None:
        self.i.append(item)
        self.w += item.w
        self.available = self.mw - self.w
        item.b = self.id
        return True
      else:
        return False
  class Item:
​
    def __init__(self, weight, bag = None):
      self.w = weight
      self.b = bag
​
  bag_dics = {}
​
  for n in range(1, bags + 1):
    bag_dics[n] = Bag(10, n)
  
  items_by_weight = {}
​
  for item in weights:
    if item not in items_by_weight.keys():
      items_by_weight[item] = [Item(item)]
    else:
      items_by_weight[item].append(Item(item))
  
  ibws = [item for lst in reversed(sorted(list(items_by_weight.keys()))) for item in items_by_weight[lst]]
​
  del items_by_weight
​
  for bag in bag_dics.values():
    for item in ibws:
      if item.b == None:
        t = bag.add(item)
​
  unbagged = [item for item in ibws if item.b == None]
​
  return len(unbagged) == 0

