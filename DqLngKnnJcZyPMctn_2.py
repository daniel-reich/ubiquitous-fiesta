
def stock_picker(prices):
  best = -1
  for i in range(len(prices)):
    for j in range(i + 1, len(prices)):
      net = prices[j] - prices[i]
      if net > best:
        best = net
  return best

