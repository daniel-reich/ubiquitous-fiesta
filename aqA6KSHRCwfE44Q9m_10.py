
def normalize(txt):
  return '{}{}!'.format(txt[0],txt[1:].lower()) if txt.isupper() else '{}{}'.format(txt[0],txt[1:].lower())

