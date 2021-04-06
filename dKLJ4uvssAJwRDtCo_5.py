
def vending_machine(products, money, product_number):
  product_found = False
  coin_list = [500, 200, 100, 50, 20, 10]
  for product in products:
    if product_number == product['number']:
      product_found = True
      product_price = product['price']
      return_dict = {'product': product['name']}
      break
  if not product_found:
    return "Enter a valid product number"
    
  if money < product_price:
    return "Not enough money for this product"
​
  coin_return = []
  remaining_change = money - product_price
  while remaining_change > 0:
    for coin in coin_list:
      if coin <= remaining_change:
        coin_return.append(coin)
        remaining_change -= coin
        break
  
  return_dict['change'] = coin_return
  
  return return_dict

