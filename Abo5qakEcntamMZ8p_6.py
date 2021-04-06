
def gimme_the_letters(spectrum):
  first, last = map(ord, spectrum.split('-'))
  return ''.join(chr(i) for i in range(first, last+1))

