
def dis(price, discount):
  finalPrice = price - ((discount / 100) * price)
  finalPrice = round(finalPrice, 2)
  return finalPrice

