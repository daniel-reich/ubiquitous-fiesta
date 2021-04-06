
def gimme_the_letters(spectrum):
  st=spectrum[0]
  la=spectrum[-1]
  return "".join([chr(x) for x in range(ord(st),ord(la)+1)])

