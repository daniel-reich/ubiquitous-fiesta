
tax = .06
def checkout(cart):
  return sum(i['prc'] * i['qty'] + i['taxable'] * i['prc']  * 0.06 * i["qty"] for i in cart)

