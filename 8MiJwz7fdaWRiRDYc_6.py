
def apocalyptic(n):
  if str(2**n).find('666') != -1:
    return 'Repent! {} days until the Apocalypse!'.format(str(2**n).find('666'))
  else:
    return 'Crisis averted. Resume sinning.'

