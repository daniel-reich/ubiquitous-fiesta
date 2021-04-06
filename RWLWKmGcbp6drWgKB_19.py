
def chosen_wine(wines):
  if len(wines)==0:
    return None
  shop = sorted([(i['name'],i['price'])for i in wines],key=lambda x: x[1])
  if len(shop)==1:
    return shop[0][0]
  return shop[1][0]

