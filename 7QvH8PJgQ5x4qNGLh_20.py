
def countdown(n, txt):
  return "{}. {}!".format(". ".join([ str(x) for x in range(n,0,-1)]), txt.upper())

