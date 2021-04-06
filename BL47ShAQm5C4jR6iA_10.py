
def third_most_expensive(dct):
  items = sorted(dct, key=dct.get, reverse=True)
  return items[2] if len(items) >= 3 else False

