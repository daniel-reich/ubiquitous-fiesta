
def apocalyptic(n):
  return "Crisis averted. Resume sinning." if str(2**n).find('666')==-1 else "Repent! " + str(str(2**n).find('666')) + " days until the Apocalypse!"

