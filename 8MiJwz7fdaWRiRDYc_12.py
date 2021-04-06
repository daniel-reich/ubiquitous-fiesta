
def apocalyptic(n):
  found = str(2**n).find('666')
  if found == -1:
    return 'Crisis averted. Resume sinning.'
  else:
    return 'Repent! {} days until the Apocalypse!'.format(found)

