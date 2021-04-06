
def apocalyptic(n):
  strN = str(2**n)
  index = strN.find("666")
  if index != -1:
    return "Repent! {0} days until the Apocalypse!".format(index)
  else:
    return "Crisis averted. Resume sinning."

