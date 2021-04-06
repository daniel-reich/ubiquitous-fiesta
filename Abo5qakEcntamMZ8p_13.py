
def gimme_the_letters(spectrum):
  return "".join(chr(x) for x in range(ord(spectrum[0]), ord(spectrum[-1]) + 1))

