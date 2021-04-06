
def third_most_expensive(dct):
  return False if len(dct) < 3 else sorted(dct.items(), key=lambda x: x[1], reverse=True)[2][0]

