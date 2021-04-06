
def expensive_orders(orders, cost):
  return {k: v for k, v in orders.items() if v > cost}

