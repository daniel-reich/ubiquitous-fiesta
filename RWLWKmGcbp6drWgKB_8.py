
def chosen_wine(wines):
  wines = sorted(wines, key=lambda x: x['price'])
  if not wines:
    return None
  elif len(wines) >= 2:
    return wines[1]['name']
  else:
    return wines[0]['name']

