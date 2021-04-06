
def get_total_price(groceries):
  def item_price(d):
  
    amount = d['quantity']
    price = d['price'] * amount
    
    return price
  
  prices = []
  
  for grocery in groceries:
    
    price = item_price(grocery)
    prices.append(price)
  
  s = sum(prices)
  
  return round(s,1)

