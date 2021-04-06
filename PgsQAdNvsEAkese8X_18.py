
def to_list(dct):
  newlist = []
  newlist2 = []
  for eachvalue in sorted(dct.keys()):
    newlist2.append(eachvalue)
    x = dct.get(eachvalue)
    newlist2.append(x)
    newlist.append(newlist2)
    newlist2 = []
  return newlist

