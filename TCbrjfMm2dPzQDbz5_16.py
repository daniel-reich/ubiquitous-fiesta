
def insert_whitespace(txt):
  return txt[0]+''.join(' '+x if x.isupper() else x for x in txt[1:])

