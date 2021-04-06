
tax = .06
def checkout(cart):
  total=0
  for i in cart:
    b=(i['prc']*i['qty'])
    if i['taxable']:b=b+(b*tax)
    total+=b
  return total

