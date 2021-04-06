
def validate_spelling(txt):
  txt=txt[:-1].replace(' ','').split('.')
  return ''.join(txt[:-1])==txt[-1].upper()

