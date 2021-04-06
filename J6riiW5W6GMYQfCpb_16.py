
def expensive_orders(d, k):
  return {key : v for key, v in d.items() if v > k}

