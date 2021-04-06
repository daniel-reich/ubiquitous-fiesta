
from itertools import permutations as p
​
class Thing:
  def __init__(self, name, weight, value):
    self.name = name
    self.weight = weight
    self.value = value
​
  def display_info(self):
    print(self.name, self.weight, self.value)
​
def knapsack(capacity, items):
  things = []
  for x in items:
    v = x['value']
    w = x['weight']
    n = x['name']
    things.append(Thing(n, w, v))
    
  combos = p(things)
  print(list(combos))

