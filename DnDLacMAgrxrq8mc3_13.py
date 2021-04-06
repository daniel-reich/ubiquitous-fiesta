
def blah_blah(txt, n):
  nt = txt.split()
  if n>len(nt):
    return "blah "*(len(nt)-1)+"blah..."
  return " ".join(nt[0:-n])+" blah"*n+"..."

