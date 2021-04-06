
def keyboard_mistakes(txt):
  return txt.translate(str.maketrans('0145', 'OIAS'))

