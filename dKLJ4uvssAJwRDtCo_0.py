
def vending_machine(products, money, num):
  if num not in range(1, 10):
    return 'Enter a valid product number'
    
  if money < products[num-1]['price']:
    return 'Not enough money for this product'
    
  money -= products[num-1]['price']
  coins = [500, 200, 100, 50, 20, 10]
  change = []
​
  for i in coins:
    change.extend([i] * (money//i))
    money %= i
  
  return {'product': products[num-1]['name'], 'change': change}

