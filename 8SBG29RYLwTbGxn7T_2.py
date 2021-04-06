
def free_shipping(order):
  return True if sum(order.values()) > 50 else False

