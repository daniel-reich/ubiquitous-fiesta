
def verbify(txt):
  l = txt.split(" ")
  if l[0].endswith("ed"): return txt
  if l[0].endswith("e"):  return "{}d {}".format(l[0],l[1])
  else: return "{}ed {}".format(l[0],l[1])

