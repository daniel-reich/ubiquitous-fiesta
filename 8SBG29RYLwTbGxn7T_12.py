
def free_shipping(order):
  if sum(order.values()) > 50:
    return True
  return False

