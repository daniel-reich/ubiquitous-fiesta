
def checkout(cart, t=.06):
  return sum(item['prc'] * item['qty'] * [1, 1.06][item['taxable']] for item in cart)

