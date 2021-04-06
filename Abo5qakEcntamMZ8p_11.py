
def gimme_the_letters(sp):
  return "".join( chr(o) for o in range( ord(sp[0]), ord(sp[2])+1 ) )

