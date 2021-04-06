
def _sorton_price(wine):
  return wine['price']
​
def chosen_wine(wines):
  if len(wines) >= 2:
    wines.sort(key=_sorton_price, reverse=False)
    return wines[1]['name']
  elif len(wines) == 0:
    return None
  else:
    return wines[0]['name']

