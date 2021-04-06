
def third_most_expensive(dct):
  if len(dct) < 3:
    return False
  else:
    newlist = []
    for eachitem in dct.keys():
      newlist.append(dct[eachitem])
    newlist.sort()
    newlist.reverse()
    third = newlist[2]
    for eachitem in dct.keys():
      if dct[eachitem] == third:
        return eachitem

