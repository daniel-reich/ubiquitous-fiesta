
def get_total_price(groceries):
  total = 0
  for i in groceries:
    #print (i)
    total = total + (i['quantity'] * i['price'])
  return round(total, 1)
    
get_total_price([
  { "product": "Milk", "quantity": 1, "price": 1.50 }
])

