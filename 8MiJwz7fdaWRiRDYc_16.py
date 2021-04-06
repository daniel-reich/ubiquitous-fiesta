
def apocalyptic(n):
  newnum = 2 ** n
  numstr = str(newnum)
  if '666' in numstr:
    location = int(numstr.find('666'))
    return("Repent! {} days until the Apocalypse!".format (location))
  else:
    return("Crisis averted. Resume sinning.")

