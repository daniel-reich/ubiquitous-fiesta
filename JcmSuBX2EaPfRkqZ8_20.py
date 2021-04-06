
def get_total_price(groceries):
  return round(sum([x["quantity"]*x["price"] for x in groceries]), 1)
​
  
# 1 bottle of milk & 1 box of cereals:
#get_total_price([
#  { "product": "Milk", "quantity": 1, "price": 1.50 },
#  { "product": "Cereals", "quantity": 1, "price": 2.50 }
#]) => 4

