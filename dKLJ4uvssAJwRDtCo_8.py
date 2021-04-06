
def vending_machine(products, money, product_number):
  if not product_number-1 in range(len(products)):return 'Enter a valid product number'
  coins=[500, 200, 100, 50, 20, 10]
  change=[products[(product_number-1)]['price']]
  if sum(change)>money:return 'Not enough money for this product'
  while sum(change)<money:
    for i in coins:
      if money-sum(change)>=i:
        change+=[i]
        break
  return {'product':products[(product_number-1)]['name'], 'change':change[1:]}

