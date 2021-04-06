
def sort_drinks_by_price(drinks):
  
  prices = []
  drink_price = {}
  
  for drink in drinks:
    price = drink['price']
    prices.append(price)
    drink_price[price] = drink
  
  prices = sorted(prices)
  drinks = []
  
  for price in prices:
    drinks.append(drink_price[price])
  
  return drinks

