
def free_shipping(order):
  return sum(order[item] for item in order) > 50

