
def verbify(txt):
  if txt.split()[0].endswith("ed"):
    return txt
  elif txt.split()[0].endswith("e"):
    return txt.split()[0]+"d" +" " + txt.split()[1]
  else:
    return txt.split()[0]+"ed" +" " + txt.split()[1]

