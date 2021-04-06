
def remove_abc(txt):
  if any(c in txt for c in ['a','b','c']):
    for c in ['a','b','c']:
      txt = txt.replace(c,'') 
    return txt
  return None

