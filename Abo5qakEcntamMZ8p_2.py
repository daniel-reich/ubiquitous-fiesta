
def gimme_the_letters(spectrum):
  start, end = [ord(i) for i in spectrum.split('-')]
  return ''.join(chr(i) for i in range(start, end+1))

