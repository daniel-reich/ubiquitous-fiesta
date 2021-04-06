
def vending_machine(products, money, product_number):
  change_coins = [500, 200, 100, 50, 20, 10]
  customer_change = []
  result = {}
  counter = 0
  for element in products:
    for key, values in element.items():
      if key == "number" and values == product_number:
        result["product"] = element["name"]
        product_price = element["price"]
        if product_price > money:
          return "Not enough money for this product"
        else:
          remainder = money - product_price 
          for number in change_coins:
            while number <= remainder:
              remainder -= number
              customer_change.append(number)
          result["change"] = customer_change
      else:
        counter += 1
        if counter == 27:
          return "Enter a valid product number"
​
  return result

