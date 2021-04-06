
def gimme_the_letters(spectrum):
  string = ''
  for i in range(ord(spectrum[0]), ord(spectrum[2]) + 1):
    string += chr(i)
  return string

