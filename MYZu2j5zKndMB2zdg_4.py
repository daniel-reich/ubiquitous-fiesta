
def absolute(txt):
  return ' '.join('an absolute' if i in 'aA' else i for i in txt.split()).capitalize()

