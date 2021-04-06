
def to_camel_case(txt):
  txt = txt.replace('-',' ').replace('_',' ').split()
  return txt[0]+''.join(x.title() for x in txt[1:]) if txt else ''

