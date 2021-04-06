
def insert_whitespace(txt):
  return txt[0]+''.join(' '+i if i.isupper() else i for i in txt[1:])

