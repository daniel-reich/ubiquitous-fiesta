
def third_most_expensive(dct):
  if len(dct) < 3:
    return False
  else:
    return sorted(dct.items(), key=lambda item: item[1], reverse = True)[2][0]

