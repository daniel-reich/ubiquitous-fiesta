
def free_shipping(order):
  prices = []
  for i in order:
    prices.append(order[i])
  if sum(prices) >= 50.00:
    return(True)
  else:
    return(False)

