
tax = .06
def checkout(cart):
  return sum( list( map( lambda x : (x['prc'] * x['qty']) * (1 + tax) if x['taxable'] else x['prc'] * x['qty'], cart  )))

