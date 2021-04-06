
def apocalyptic(n):
  index = str(2 ** n).find('666');
  return "Crisis averted. Resume sinning." if index == - 1 else "Repent! {} days until the Apocalypse!".format(index)

