
def apocalyptic(n):
  try:
    return 'Repent! ' + str(str(2**n).index('666')) + ' days until the Apocalypse!'
  except ValueError:
    return "Crisis averted. Resume sinning."

