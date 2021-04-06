
def gimme_the_letters(spectrum):
  nl = spectrum.split('-')
  a, b = nl[0], nl[1]
  return ''.join(chr(i) for i in range(ord(a), ord(b)+1))

