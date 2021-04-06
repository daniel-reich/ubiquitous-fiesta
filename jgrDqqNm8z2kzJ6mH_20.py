
tax = .06
def checkout(cart):
  tot = 0
  for item in cart:
    if item["taxable"] == True:
      tot = tot + item['prc']*item['qty']*(1+tax)
    else:
      tot = tot + item['prc']*item['qty']
  return tot

