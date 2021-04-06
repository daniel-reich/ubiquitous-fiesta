
def chosen_wine(wines):
  print(wines)
  if wines == []:
    return None
  elif len(wines) == 1:
    return wines[0]['name']
  else:
    newlist = []
    for eachwine in wines:
      newlist.append(eachwine['price'])
    themin = sorted(newlist)[1]
    for eachwine in wines:
      if eachwine['price'] == themin:
        return eachwine['name']

