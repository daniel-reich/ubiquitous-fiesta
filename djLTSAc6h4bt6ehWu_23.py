
def camelCasing(txt):
  txt = txt.replace('_',' ').split()
  return txt[0].lower() + ''.join( [ w.title() for w in txt[1:] ] )

