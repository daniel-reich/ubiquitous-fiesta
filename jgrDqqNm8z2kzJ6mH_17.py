
tax = .06
def checkout(cart):
  return sum(i['prc']*i['qty']*(1.06 if i['taxable'] else 1) for i in cart)

