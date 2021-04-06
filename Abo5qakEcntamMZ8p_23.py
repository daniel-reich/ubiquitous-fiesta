
def gimme_the_letters(spectrum):
  s = spectrum.split('-')
  return ''.join(chr(x) for x in range(ord(s[0]), ord(s[1])+1))

