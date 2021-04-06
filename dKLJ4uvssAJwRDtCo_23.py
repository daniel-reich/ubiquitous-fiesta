
class Product:
  def __init__(self,number):
    self.product = products[number-1]
  def name(self):
    return self.product["name"]
  def price(self):
    return self.product["price"]
​
​
def vending_machine(products, money, product_number):
  p = Product(product_number)
  if product_number < 1 or product_number > 9:
    return "Enter a valid product number"
  elif p.price() > money:
    return "Not enough money for this product"
  else:
    product = p.name()
    remaining = money - p.price()
    coins = [500,200,100,50,20,10]
    change = []
    for coin in coins:
      if coin <= remaining:
        for k in range(0,remaining//coin):
          change.append(coin) 
          remaining -= coin
    return {'product':product,'change':change}

