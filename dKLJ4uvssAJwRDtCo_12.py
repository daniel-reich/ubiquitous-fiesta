
COINS = [500, 200, 100, 50, 20, 10]
def vending_machine(products, money, product_number):
  p = [x for x in products if x['number'] == product_number]
  if not p:
    return "Enter a valid product number"
  price = p[0]['price']
  if money < price:
    return "Not enough money for this product"
  change = [] if money == price else getChange(money-price)
  return { "product": p[0]['name'], "change": change}
​
def getChange(amount):
  a = []
  for c in COINS:
    while (amount >= c):
      a.append(c)
      amount -= c
  return a

