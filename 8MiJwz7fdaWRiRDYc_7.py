
def apocalyptic(n):
  x = 2**n
  x = str(x)
  if "666" in x:
    return "Repent! {} days until the Apocalypse!".format(x.index("666"))
  else:
    return "Crisis averted. Resume sinning."

