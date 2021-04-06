
def free_shipping(order):
  if sum(order.values()) > 50:
    return True
  else: return False

