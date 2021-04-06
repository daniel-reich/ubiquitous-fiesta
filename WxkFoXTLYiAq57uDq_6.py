
def find_and_remove(dct):
  for room,items in dct.items():
    for item,price in items.items():
      try:
        dct[room][item] = int(price)
      except:
        dct[room][item] = -1
    dct[room] = {k:v for k,v in items.items() if v > 0}
  return dct

