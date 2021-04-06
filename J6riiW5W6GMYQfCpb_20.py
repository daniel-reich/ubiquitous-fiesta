
def expensive_orders(d, k):
  return {a:b for a,b in d.items() if b > k}

