
def vending_machine(products, money, product_number):
  if 1 > product_number < 9:
    return "Enter a valid product number"
  elif products[product_number - 1]["price"] > money:
    return "Not enough money for this product"
  
  product = products[product_number - 1]["name"]
  price = products[product_number - 1]["price"]
  changes = [500, 200, 100, 50, 20, 10]
  change = []
  
  while sum(change) < (money - price):
    for i in range(len(changes)):
      if changes[i] + sum(change) > (money - price):
        changes.pop(i)
        break
      else:
        change.append(changes[i])
        break
  
  return {"product": product, "change": change}

