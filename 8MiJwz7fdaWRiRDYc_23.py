
def apocalyptic(n):
  days = str(2**n).find('666')
  if days >= 0:
    return 'Repent! {} days until the Apocalypse!'.format(days)  
  else:
    return "Crisis averted. Resume sinning."

