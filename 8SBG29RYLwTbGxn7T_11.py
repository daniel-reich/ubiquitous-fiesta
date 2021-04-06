
def free_shipping(order):
 total = order.values
 if sum(total()) > 50.00:
   return True
 else:
   return False

