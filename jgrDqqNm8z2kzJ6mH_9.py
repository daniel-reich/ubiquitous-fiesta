
def checkout(cart):
  return sum(x['prc']*x['qty']*(1.06 if x['taxable'] else 1) for x in cart)

