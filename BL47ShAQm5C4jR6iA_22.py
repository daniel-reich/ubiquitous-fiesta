
def third_most_expensive(dct):
  if len(dct.items()) < 3:
    return False
  return sorted((k for k in dct.keys()),key=lambda x: -dct[x])[2]

