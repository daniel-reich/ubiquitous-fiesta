
def expensive_orders(d, amount):
  return {k: v for k, v in d.items() if v > amount}

