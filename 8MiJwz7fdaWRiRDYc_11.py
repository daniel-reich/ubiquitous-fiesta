
def apocalyptic(n):
  power = 2**n
  if '666' in str(power):
    ind = str(power).index('666')
    return "Repent! " + str(ind) + " days until the Apocalypse!"
  return "Crisis averted. Resume sinning."

