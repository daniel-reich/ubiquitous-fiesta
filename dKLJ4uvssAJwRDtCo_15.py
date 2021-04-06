
coins = [500, 200, 100, 50, 20, 10]
def vending_machine(products, money, product_number):
  products =  filter(lambda p: p['number'] == product_number, products)
  product = next(products, None)
  if product is None:
    return "Enter a valid product number"
  money -= product['price']
  if money < 0:
    return "Not enough money for this product"
  change = []
  for coin in coins:
    change.extend([coin] * (money // coin))
    money %= coin
  return {'product':product['name'], 'change':change}

