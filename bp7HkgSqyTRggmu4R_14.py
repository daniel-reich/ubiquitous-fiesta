
def reverse_title(txt):
  return ' '.join([i[0].lower()+i[1:].upper() for i in txt.split()])

