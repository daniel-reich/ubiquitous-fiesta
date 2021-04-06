
def chosen_wine(wines):
  if wines:
    if len(wines)==1: return wines[0]['name']
    else:
      price = sorted([wines[i]['price'] for i in range(len(wines))])[1]
      for i in wines:
        if i['price']==price: return i['name']
  else: return None

