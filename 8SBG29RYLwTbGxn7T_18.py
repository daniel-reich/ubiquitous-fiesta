
def free_shipping(order):
  return bool(sum(order.values()) > 50)

