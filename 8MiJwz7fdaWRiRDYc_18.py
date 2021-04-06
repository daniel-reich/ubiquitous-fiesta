
def apocalyptic(n):
  if '666' in str(2**n):
    return 'Repent! {} days until the Apocalypse!'.format(str(2**n).index('666'))
  return 'Crisis averted. Resume sinning.'

