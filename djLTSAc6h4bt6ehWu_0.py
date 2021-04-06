
def camelCasing(txt):
  txt=txt.title().replace('_','').replace(' ','')
  return txt[0].lower()+txt[1:]

