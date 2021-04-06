
def expensive_orders(d, k):
  return {q:v for (q,v) in d.items() if v>k}

