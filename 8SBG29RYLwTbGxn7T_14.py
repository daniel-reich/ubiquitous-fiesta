
def free_shipping(order):
  total = 0
  for item in order.values():
    total += item
  return total > 50

