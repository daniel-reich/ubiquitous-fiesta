
def verbify(txt):
  if str(txt.split()[0])[-1] in ['a', 'e', 'i', 'o', 'u']:
    return str(txt.split()[0]) + "d " + str(txt.split()[1])
  elif str(txt.split()[0])[-2:] == "ed":
    return txt  
  else:
    return str(txt.split()[0]) + "ed " + str(txt.split()[1])

