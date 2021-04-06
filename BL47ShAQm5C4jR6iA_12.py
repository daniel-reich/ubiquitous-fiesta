
def third_most_expensive(dct):
  if len(dct) < 3:
    return False
  price = sorted(dct.values())[-3]
  for item in dct:
    if price == dct[item]:
      return item

