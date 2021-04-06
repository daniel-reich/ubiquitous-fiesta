
def checkout(cart):
  total = 0
  for c in cart:
    price = c['prc'] * c['qty']
    total += 1.06 * price if c['taxable'] else price
  return total

