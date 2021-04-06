
def third_most_expensive(dct):
  dct_values = list(dct.values())
  dct_values.sort(reverse=True)
  try:
    value = dct_values[2]
    for x, y in dct.items():
      if y == value:
        return x
  except:
    return False

