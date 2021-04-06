
def verbify(txt):
  lst = txt.split()
  if lst[0].endswith("e"): return lst[0] +"d " + lst[1]
  if lst[0].endswith("d"): return lst[0] +" " + lst[1]
  return lst[0] +"ed " + lst[1]

