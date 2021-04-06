
def chosen_wine(wines):
  if not wines:
    return None
  if len(wines) == 1:
    return wines[0]['name']
  r = sorted([(float(i['price']), i['name']) for i in wines])
  return r[1][1]

