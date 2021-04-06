
def checkout(cart):
  total=0
  for i in cart:
    cur=i['prc']*i['qty']
    if i['taxable']:
      cur*=1.06
    total+=cur
  return total

