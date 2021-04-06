
def expensive_orders(d, k):
  return {key:value for key, value in d.items() if value > k}

