
def maskify(txt):
  if len(txt)<5:
    return txt
  else:
    return((len(txt)-4)*'#'+txt[(len(txt)-4):len(txt)])

