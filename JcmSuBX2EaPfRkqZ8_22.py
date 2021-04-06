
def get_total_price(groceries):
  sum = 0
  tempPrice = 0
  for i in range(len(groceries)):
    quantity = groceries[i].get("quantity")
    price = groceries[i].get("price")
    tempPrice = quantity * price
    sum = sum + tempPrice
    
  return round(sum,1)

