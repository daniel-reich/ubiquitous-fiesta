
def apocalyptic(n):
  number = 2 ** n
  apoc = str(number).find('666')
  if apoc == -1:
    return "Crisis averted. Resume sinning."
  else:
    return "Repent! {} days until the Apocalypse!".format(apoc)

