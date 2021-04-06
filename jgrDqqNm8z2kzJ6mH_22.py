
tax = .06
def checkout(cart):
  total = 0
  for i in cart:
    a = (i.get('qty')*i.get('prc'))
    if i.get('taxable') == True:
      a = a + (a*tax)
    total += a
  return total

