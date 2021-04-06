
def apocalyptic(n):
  for i,j in enumerate(str(2**n)):
    if j in '6':
      if str(2**n)[i+1] in '6':
        if str(2**n)[i+2] in '6':
          return "Repent! {} days until the Apocalypse!".format(i)
  return "Crisis averted. Resume sinning."

