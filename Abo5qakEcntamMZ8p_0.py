
def gimme_the_letters(sp):
  return "".join(chr(n) for n in range(ord(sp[0]),ord(sp[-1])+1))

