
def apocalyptic(n):
  if str(2**n).find('666') == -1:
    return "Crisis averted. Resume sinning."
  else:
    return 'Repent! ' + str(str(2**n).find('666')) + ' days until the Apocalypse!'

