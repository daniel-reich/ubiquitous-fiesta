
def apocalyptic(n):
  armageddon = str(2**n).find("666")
  return "Repent! {} days until the Apocalypse!".format(armageddon) if armageddon >= 0 else "Crisis averted. Resume sinning."

