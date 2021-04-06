
def apocalyptic(n):
  no = pow(2, n)
  if str(no).count('666') > 0:
    return "Repent! {} days until the Apocalypse!".format(str(no).index('666'))
  else:
    return "Crisis averted. Resume sinning."

