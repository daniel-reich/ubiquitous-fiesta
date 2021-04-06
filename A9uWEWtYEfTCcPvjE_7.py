
def price_importance_sort(dct, b):
​
  class Item:
​
    def __init__(self, name, price, importance):
      self.name = name
      self.price = price
      self.imp = importance
    
  class Budget:
​
    def __init__(self, budget):
      self.budget = budget
    
    def best_purchase(self, items):
      from itertools import permutations as c
     # print(len(items), items)
      combinations = []
​
      for n in range(1, len(items) + 1):
      #  print(n)
        p = list(c(range(len(items)), n))
       # print(p)
        for item in p:
          combinations.append(item)
      
      valid_purchases = []
​
      for comb in combinations:
        if [items[c] for c in comb] not in valid_purchases and list(reversed([items[c] for c in comb])) not in valid_purchases:
          purchase = [items[c] for c in comb]
​
      
          total_price = 0
          for item in purchase:
            total_price += item.price
          if total_price <= self.budget:
            valid_purchases.append(purchase)
      
      important_values = {}
      budget_costs = {}
​
      for purchase in valid_purchases:
        importance = 0
        for i in purchase:
          #print(i)
          importance += i.imp
        if importance not in important_values.keys():
          important_values[importance] = [purchase]
        else:
          important_values[importance].append(purchase)
        price = sum([i.price for i in purchase])
        budget_costs[str(purchase)] = price
      
      if len(important_values[max(list(important_values.keys()))]) == 1:
        return [i.name for i in important_values[max(list(important_values.keys()))][0]]
      else:
        minim = self.budget
        to_go = None
​
        for item in important_values[max(list(important_values.keys()))]:
          if budget_costs[str(item)] < minim:
            to_go = item
            minim = budget_costs[str(item)]
        
        tr = [i.name for i in to_go]
​
        return sorted(tr)
  
  items = []
​
  for item in dct.keys():
    items.append(Item(item, dct[item]['price'], dct[item]['importance']))
  
  budget = Budget(b)
​
  return budget.best_purchase(items)

