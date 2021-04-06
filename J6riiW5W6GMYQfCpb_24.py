
def expensive_orders(d, k):
  return {x:y for x,y in d.items() if y>k}

