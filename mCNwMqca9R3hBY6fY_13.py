
def make_happy(txt):
  if len(txt)<2:
    return txt
  else:
    cr = "x8:;"
    idx = [txt.index(x) for x in txt if x in cr]
    z = [')' if txt[x] == '(' else txt[x] for x in range(idx[0], len(txt))]
    return txt[:idx[0]]+"".join(z)

