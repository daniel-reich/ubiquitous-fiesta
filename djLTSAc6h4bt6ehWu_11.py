
def camelCasing(txt):
  return txt[0].lower() + ''.join(i.capitalize() for i in (' '.join(txt.split('_'))).split())[1:]

