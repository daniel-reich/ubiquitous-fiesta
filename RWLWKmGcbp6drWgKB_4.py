
def chosen_wine(wines):
  if len(wines) == 1:
    chosen = wines[0]['name']
  elif len(wines) == 0:
    chosen = None
  else:
    prices_first = []
    for wine_dict in wines:
      prices_first.append([wine_dict['price'], wine_dict['name']])
    prices_first.sort()
    chosen = prices_first[1][1]
  return chosen

