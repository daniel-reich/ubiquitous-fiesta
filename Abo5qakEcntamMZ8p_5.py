
def gimme_the_letters(spectrum):
  return ''.join(chr(i) for i in range(ord(spectrum[0]), ord(spectrum[-1]) + 1))

