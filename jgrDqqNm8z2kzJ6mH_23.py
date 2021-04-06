
tax = .06
def checkout(cart):
  return sum(i['prc']*i['qty']*(1+tax*i['taxable']) for i in cart)

