
def third_most_expensive(dct):
  sort_dct = list(sorted(dct, key=dct.get))
  return sort_dct[-3] if len(sort_dct)>2 else False

