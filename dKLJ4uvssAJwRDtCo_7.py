
def vending_machine(products, money, num):
  if num not in range(1, 10):
    return "Enter a valid product number"
  name = products[num -1]['name']
  price = products[num -1]['price']
  diff = money - price
  if diff == 0:
    return {"product": name, "change": []}
  if diff < 0:
    return "Not enough money for this product"
​
  coins = [500, 200, 100, 50, 20, 10]
  change = []
  for coin in coins:
    if diff > 0:
      times = diff // coin
      diff -= times * coin
      change.append(times * [coin])
  change = [i for lst in change for i in lst]
  return {"product": name, "change": change}

