
def expensive_orders(d, k):
  return {a: v for a, v in d.items() if v > k}

