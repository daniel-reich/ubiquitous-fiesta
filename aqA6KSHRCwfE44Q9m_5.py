
def normalize(txt):
  if all(all(i.isupper() for i in x) for x in txt.split(' ')):
    return (txt.lower()).capitalize() + '!'
  return txt

