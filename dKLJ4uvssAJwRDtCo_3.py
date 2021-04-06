
def vending_machine(products, money, product_number):
  if product_number not in range(1, len(products)+1):
    return "Enter a valid product number"
  product = products[product_number-1]
  owed = money - product['price']
  if owed < 0:
    return "Not enough money for this product"
  coins = []
  denoms = [500, 200, 100, 50, 20, 10]
  i = 0
  while owed > 0:
    while owed < denoms[i]:
      i += 1
    coins.append(denoms[i])
    owed -= denoms[i]
  return {'change' : coins, 'product' : product['name']}

