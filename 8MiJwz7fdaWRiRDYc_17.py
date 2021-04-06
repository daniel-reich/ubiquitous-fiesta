
def apocalyptic(n):
  if '666' in str(2 ** n):
    return 'Repent! {} days until the Apocalypse!'.format(str(2 ** n).find('666'))
  else:
    return 'Crisis averted. Resume sinning.'

