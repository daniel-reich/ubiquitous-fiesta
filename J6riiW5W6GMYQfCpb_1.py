
def expensive_orders(d, k):
  result = {}
  for key, value in d.items():
    if value > k:
      result[key] = value
  return result

