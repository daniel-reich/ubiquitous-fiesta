
def verbify(txt):
  word = txt[:txt.find(' ')]
  word = word if word[-2:] == 'ed' else word + 'd' if word[-1] == 'e' else word + 'ed'
  return word + txt[txt.find(' '):]

