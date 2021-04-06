
def insert_whitespace(txt):
  return ''.join([' '+x if x == x.upper() else x for x in txt])[1:]

