
tax = .06
def checkout(cart):
  price = 0
  for i in cart:
    temp = i['prc']*i['qty']
    if i['taxable']:
      price+=temp+(temp*tax)
    else:
      price+=temp
  return price

