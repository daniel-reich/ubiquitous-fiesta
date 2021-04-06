
def insert_whitespace(txt):
  return "".join([(" "+i) if i.isupper() else i for i in txt ])[1:]

