
def apocalyptic(n):
  num = str(2**n)
  if num.find('666') == -1:
    return "Crisis averted. Resume sinning."
  else:
    return "Repent! {} days until the Apocalypse!".format(num.find('666'))

