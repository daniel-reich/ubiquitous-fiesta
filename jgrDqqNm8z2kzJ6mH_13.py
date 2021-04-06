
tax = .06
def checkout(cart):
  return sum([a[0]+(a[0]*a[1]) for a in [(x['prc']*x['qty'],x['taxable']*tax) for x in cart]])

