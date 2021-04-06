
def vending_machine(products, money, product_number):
  desired = [p for p in products if p['number'] == product_number]
  if not desired: return 'Enter a valid product number'
  
  change = money - desired[0]['price']
  if change<0: return "Not enough money for this product"
  
  change_lst = []
  for coin in [500, 200, 100, 50, 20, 10]:
    while change>=coin:
      change_lst+= [coin]
      change-= coin
​
  return {'product':desired[0]['name'], 'change': change_lst}

