
def third_most_expensive(dct):
  try:
    return sorted(dct.items(), key=lambda d: d[1], reverse=True)[2][0]
  except IndexError:
    return False

