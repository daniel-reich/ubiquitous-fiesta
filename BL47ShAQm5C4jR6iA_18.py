
def third_most_expensive(dct):
  if len(dct) < 3:
    return False
  return [(v, k) for k, v in sorted(dct.items(), key=lambda x: x[1])][-3][1]

