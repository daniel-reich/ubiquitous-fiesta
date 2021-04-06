
def gimme_the_letters(spectrum):
  a = spectrum.split('-')
  r1 = ord(a[0])-96
  r2 = ord(a[1])-96
  return ''.join(chr(i+96) for i in range(r1, r2+1))

