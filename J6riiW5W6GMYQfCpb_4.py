
def expensive_orders(d, k):
  return {i:d[i] for i in d if d[i] > k}

