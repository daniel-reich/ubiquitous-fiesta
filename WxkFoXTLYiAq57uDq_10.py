
def find_and_remove(dct):
  nd = {}
  
  for k in dct.keys():
    d = dct[k]
    nn = {}
    for ke in d.keys():
      try:
        nn[ke] = int(d[ke])
      except ValueError:
        continue
    nd[k] = nn
  
  return nd

