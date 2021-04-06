
def free_shipping(order):
  tot = 0
  for key, value in order.items():
    tot += int(value)
  return tot >= 50

